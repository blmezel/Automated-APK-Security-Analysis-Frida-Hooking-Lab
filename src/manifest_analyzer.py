#!/usr/bin/env python3
"""
Module: Android Manifest Static Analyzer
Description: Parses AndroidManifest.xml to identify security misconfigurations.
"""

import xml.etree.ElementTree as ET
from colorama import init, Fore, Style

# Initialize terminal colors
init(autoreset=True)

def analyze_manifest(file_path):
    print(Fore.CYAN + Style.BRIGHT + f"\n[*] Starting static analysis on: {file_path}")
    
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        android_ns = '{http://schemas.android.com/apk/res/android}'
        
        app_tag = root.find('application')
        if app_tag is not None:
            print(Fore.BLUE + "[*] Inspecting <application> tag attributes...")
            
            # 1. Check if application is debuggable (Critical for Reverse Engineering)
            debuggable = app_tag.get(f'{android_ns}debuggable')
            if debuggable == 'true':
                print(Fore.RED + "  [!] HIGH VULNERABILITY: Application is debuggable (android:debuggable='true').")
            else:
                print(Fore.GREEN + "  [+] Secure: Application is not debuggable.")

            # 2. Check for cleartext traffic (Network Security)
            cleartext = app_tag.get(f'{android_ns}usesCleartextTraffic')
            if cleartext == 'true':
                print(Fore.RED + "  [!] HIGH VULNERABILITY: Cleartext traffic is allowed. MITM attacks possible.")
            else:
                print(Fore.GREEN + "  [+] Secure: Cleartext traffic is disabled.")

            # 3. Check if backup is allowed (Data Leakage)
            allow_backup = app_tag.get(f'{android_ns}allowBackup')
            if allow_backup == 'true':
                print(Fore.YELLOW + "  [!] MEDIUM WARNING: Application allows backup (android:allowBackup='true'). Data extraction possible via ADB.")
            else:
                print(Fore.GREEN + "  [+] Secure: Application backup is disabled.")

        print(Fore.CYAN + Style.BRIGHT + "[*] Manifest static analysis completed.\n")

    except FileNotFoundError:
        print(Fore.RED + f"[-] Error: Target file not found at {file_path}")
    except ET.ParseError:
        print(Fore.RED + "[-] Error: Failed to parse XML structure. Ensure it is a valid AndroidManifest.xml.")

if __name__ == "__main__":
    # Test execution
    target_xml = "src/sample_manifest.xml"
    analyze_manifest(target_xml)
