#!/usr/bin/env python3
"""
Module: Source Code Secret Scanner
Description: Scans source files (Java/Smali) for hardcoded secrets, API keys, and passwords.
"""

import re
import os
from colorama import init, Fore, Style

init(autoreset=True)

# Regex patterns for common secrets
PATTERNS = {
    "Google API Key": r"AIza[0-9A-Za-z-_]{35}",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Hardcoded Password": r"(?i)(password|passwd|pwd)\s*=\s*['\"]([^'\"]+)['\"]",
    "Generic Secret": r"(?i)(secret|api_key|token)\s*=\s*['\"]([^'\"]+)['\"]"
}

def scan_file(file_path):
    print(Fore.CYAN + Style.BRIGHT + f"\n[*] Starting static source code analysis on: {file_path}")
    
    if not os.path.exists(file_path):
        print(Fore.RED + f"[-] Error: Target file not found at {file_path}")
        return

    findings = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line_num, line in enumerate(lines, 1):
        for vulnerability, pattern in PATTERNS.items():
            match = re.search(pattern, line)
            if match:
                findings += 1
                print(Fore.RED + f"  [!] VULNERABILITY FOUND: {vulnerability}")
                print(Fore.YELLOW + f"      Line {line_num}: {line.strip()}")

    if findings == 0:
        print(Fore.GREEN + "  [+] Secure: No hardcoded secrets detected in this file.")
    else:
        print(Fore.MAGENTA + f"[*] Scan completed. Total secrets found: {findings}\n")

if __name__ == "__main__":
    # Test execution
    target_code = "src/sample_auth.java"
    scan_file(target_code)
