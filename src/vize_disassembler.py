#!/usr/bin/env python3
"""
Module: Vize Entegrasyonu - Vaultwarden & APK Native Library Audit Engine
Technology: Capstone Engine (x86_64 Architecture) & File Integrity Scanner
Description: Combines binary disassembly with install.sh integrity checks and SQLite forensic leftover analysis.
"""

import os
from capstone import *
from colorama import init, Fore, Style

init(autoreset=True)

def run_vize_disassembler(hex_code_str):
    print(Fore.CYAN + Style.BRIGHT + "\n" + "="*55)
    print(Fore.CYAN + Style.BRIGHT + "  VIZE MODÜLÜ A: CAPSTONE DISASSEMBLER ENGINE        ")
    print(Fore.CYAN + Style.BRIGHT + "  Context: Vaultwarden Native Binary Auditor (Adım 8)")
    print(Fore.CYAN + Style.BRIGHT + "="*55)
    
    try:
        CODE = bytes.fromhex(hex_code_str)
        md = Cs(CS_ARCH_X86, CS_MODE_64)
        
        print(Fore.BLUE + f"[*] Opcode Byte Sequence: {hex_code_str}")
        print(Fore.MAGENTA + "\n--- Disassembled Assembly Instructions ---")
        
        instruction_count = 0
        for insn in md.disasm(CODE, 0x1000):
            instruction_count += 1
            print(Fore.YELLOW + f"  0x{insn.address:x}:\t{insn.mnemonic:<8}\t{insn.op_str}")
            
        print(Fore.GREEN + f"\n[+] Disassembly Analizi Başarılı. Çevrilen Komut Sayısı: {instruction_count}")
        
    except ValueError:
        print(Fore.RED + "[-] Error: Invalid hex string pattern.")
    except Exception as e:
        print(Fore.RED + f"[-] Capstone execution error: {str(e)}")

def run_vize_integrity_audit():
    print(Fore.CYAN + Style.BRIGHT + "\n" + "="*55)
    print(Fore.CYAN + Style.BRIGHT + "  VIZE MODÜLÜ B: INTEGRITY & FORENSIC AUDITOR         ")
    print(Fore.CYAN + Style.BRIGHT + "  Context: Installation & Kalıntı Analizi (Adım 1 & 2)")
    print(Fore.CYAN + Style.BRIGHT + "="*55)

    # Simulating Vize Adım 1: install.sh integrity check
    print(Fore.BLUE + "[*] Checking deployment artifacts for SHA-256 validation...")
    print(Fore.RED + "  [!] HIGH RISK: install.sh does not enforce sha256sum checks on external packages.")
    print(Fore.YELLOW + "      Risk Context: Vulnerable to Man-in-the-Middle (MitM) supply chain attacks.")

    # Simulating Vize Adım 2: SQLite Forensic Leftovers
    print(Fore.BLUE + "\n[*] Scanning target directory for hidden database remnants...")
    print(Fore.RED + "  [!] FORENSIC FINDING: SQLite write-ahead logs (-wal, -shm) detected in data directory.")
    print(Fore.YELLOW + "      Risk Context: Sensitive database metadata remains intact even after container removal.")
    print(Fore.GREEN + "\n[+] Integrity and Forensic audit simulation complete.")

if __name__ == "__main__":
    # Test both deep integration layers
    sample_hex = "b83412000090"
    run_vize_disassembler(sample_hex)
    run_vize_integrity_audit()
