#!/usr/bin/env python3
"""
Module: Frida Device & Hooking Manager
Description: Manages the connection to the Android device and prepares the Frida injection environment.
"""

import frida
import sys
from colorama import init, Fore, Style

# Initialize terminal colors
init(autoreset=True)

def enumerate_devices():
    print(Fore.CYAN + Style.BRIGHT + "\n[*] Phase 6: Initializing Dynamic Analysis Environment...")
    print(Fore.BLUE + "[*] Probing for available Frida devices (Local/USB/Emulator)...")
    
    try:
        devices = frida.enumerate_devices()
        if not devices:
            print(Fore.RED + "[-] No devices found. Is ADB connected?")
            return

        for device in devices:
            # We highlight USB or Emulator devices usually used for testing
            if device.type in ['usb', 'local']:
                print(Fore.GREEN + f"  [+] Found Device: {device.name} (ID: {device.id} | Type: {device.type})")
            else:
                print(Style.DIM + f"  [-] Other Device: {device.name} (Type: {device.type})")
        
        print(Fore.MAGENTA + "\n[*] Frida environment is stable. Ready for payload injection (Hooking).")
        
    except frida.ServerNotRunningError:
        print(Fore.RED + "[-] Error: frida-server is not running on the target device.")
        print(Fore.YELLOW + "  [!] Please push frida-server to /data/local/tmp/ and execute it.")
    except Exception as e:
        print(Fore.RED + f"[-] Unexpected Error connecting to Frida: {str(e)}")

if __name__ == "__main__":
    enumerate_devices()
