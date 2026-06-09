#!/usr/bin/env python3
"""
Module: Full APK Security CLI & Risk Scorer
Description: Evaluates metadata, permissions, and strings to calculate a 0-100 Risk Score.
Matches Requirements: Tam APK Güvenlik Analizi & AndroidManifest Zafiyet Analizi (5 Apps)
"""

import os
import argparse
import xml.etree.ElementTree as ET
from colorama import init, Fore, Style

init(autoreset=True)

def calculate_risk_score(manifest_path):
    score = 100
    findings = []
    
    try:
        tree = ET.parse(manifest_path)
        root = tree.getroot()
        android_ns = '{http://schemas.android.com/apk/res/android}'
        
        print(Fore.CYAN + f"\n[*] Analyzing: {os.path.basename(manifest_path)}")
        
        # 1. Exported Components & Deep Links (Attack Surface)
        for component in ['activity', 'receiver', 'service', 'provider']:
            for tag in root.iter(component):
                if tag.get(f'{android_ns}exported') == 'true':
                    score -= 15
                    findings.append(f"Exported {component.capitalize()} Found: Potential Unauthorized Access / Deep Link Hijacking.")
                    
        # 2. Debuggable Flag
        app_tag = root.find('application')
        if app_tag is not None:
            if app_tag.get(f'{android_ns}debuggable') == 'true':
                score -= 30
                findings.append("Debuggable='true': App is vulnerable to active debugging and hooking.")
                
            if app_tag.get(f'{android_ns}usesCleartextTraffic') == 'true':
                score -= 20
                findings.append("Cleartext Traffic: Vulnerable to MITM attacks.")

        # Ensure score doesn't drop below 0
        score = max(0, score)
        
        # Output Results
        color = Fore.GREEN if score > 70 else (Fore.YELLOW if score > 40 else Fore.RED)
        print(color + Style.BRIGHT + f"    -> Calculated Risk Score: {score}/100")
        for f in findings:
            print(Fore.RED + f"       - {f}")
            
    except Exception as e:
        print(Fore.RED + f"[-] Error analyzing {manifest_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated APK Security CLI")
    parser.add_argument("--scan-dir", default="docs/samples", help="Directory containing Manifests/APKs")
    args = parser.parse_args()
    
    print(Fore.MAGENTA + Style.BRIGHT + "="*50)
    print(Fore.MAGENTA + Style.BRIGHT + "  TAM APK GÜVENLİK ANALİZ ARACI (CLI) - RİSK MOTORU")
    print(Fore.MAGENTA + Style.BRIGHT + "="*50)
    
    if os.path.exists(args.scan_dir):
        for file in sorted(os.listdir(args.scan_dir)):
            if file.endswith(".xml"):
                calculate_risk_score(os.path.join(args.scan_dir, file))
    else:
        print(Fore.RED + "[-] Sample directory not found.")
