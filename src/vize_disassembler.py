#!/usr/bin/env python3
"""
Module: Deep Vize Integration - Capstone Binary Parser & Supply Chain Auditor
Technology: Capstone Engine (x86_64) & Forensic Artifact Analyzer
Course: Reverse Engineering (BGT210)
"""

import os
import hashlib
from capstone import *
from colorama import init, Fore, Style

init(autoreset=True)

class VizeVaultwardenAuditor:
    def __init__(self):
        self.target_dir = "reports"
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)

    def audit_binary_code(self, hex_code_str):
        """[Vize Adım 8 Entegrasyonu] Disassembles native binary slices into Assembly."""
        print(Fore.CYAN + Style.BRIGHT + "\n" + "="*60)
        print(Fore.CYAN + Style.BRIGHT + "  VIZE MODÜLÜ I: NATIVE ASM DISASSEMBLER (CAPSTONE x86_64) ")
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        
        try:
            binary_data = bytes.fromhex(hex_code_str)
            # Core integration matching x86_64 micro-architecture analysis
            md = Cs(CS_ARCH_X86, CS_MODE_64)
            
            print(Fore.BLUE + f"[*] Target Stream Opcode: {hex_code_str}")
            print(Fore.MAGENTA + "--- Direct Instruction Flow ---")
            
            for insn in md.disasm(binary_data, 0x1000):
                print(Fore.YELLOW + f"  0x{insn.address:x}:\t{insn.mnemonic:<8}\t{insn.op_str}")
                
        except Exception as e:
            print(Fore.RED + f"[-] Binary disassembly failure: {str(e)}")

    def audit_supply_chain(self):
        """[Vize Adım 1 Entegrasyonu] Audits deployment scripts for signature bypass."""
        print(Fore.CYAN + Style.BRIGHT + "\n" + "="*60)
        print(Fore.CYAN + Style.BRIGHT + "  VIZE MODÜLÜ II: SUPPLY CHAIN & SCRIPT INTEGRITY SCANNER  ")
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        
        fake_install_script = os.path.join(self.target_dir, "install.sh")
        with open(fake_install_script, "w") as f:
            f.write("#!/bin/bash\ncurl -sSL https://unverified-source.com/release.tar.gz | tar -xz\n")
            
        print(Fore.BLUE + f"[*] Scanning setup script integrity: {fake_install_script}")
        
        with open(fake_install_script, "r") as f:
            content = f.read()
            
        # Forensic validation: Looking for dangerous unverified execution loops
        if "sha256sum" not in content:
            print(Fore.RED + "  [!] CRITICAL SECURITY BREACH (MitM): install.sh pulls remote data without strict SHA-256 verification loops.")
            print(Fore.YELLOW + "      Exploitation Context: Package injection / Supply chain interception vectors identified.")
        else:
            print(Fore.GREEN + "  [+] Secure: Script implements integrity hash loops.")

    def audit_forensic_leftovers(self):
        """[Vize Adım 2 Entegrasyonu] Simulates SQLite residual database forensic logging."""
        print(Fore.CYAN + Style.BRIGHT + "\n" + "="*60)
        print(Fore.CYAN + Style.BRIGHT + "  VIZE MODÜLÜ III: SQLITE FORENSIC ARTIFACT DETECTION      ")
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        
        # Dropping a physical forensic remnant file to simulate dirty unlinking vectors
        remnant_file = os.path.join(self.target_dir, "vaultwarden.db-wal")
        with open(remnant_file, "w") as f:
            f.write("SQLITE WAL residual metadata stream leak test.")
            
        print(Fore.BLUE + "[*] Monitoring directory tree for structural residual exposures...")
        if os.path.exists(remnant_file):
            print(Fore.RED + f"  [!] ADLİ BİLİŞİM BULGUSU: Active write-ahead cache logging structure found: '{remnant_file}'")
            print(Fore.YELLOW + "      Exploitation Context: Host memory leak path. Cryptographic keys can be salvaged from WAL frames.")
            
        print(Fore.GREEN + "\n[+] Deep-level architectural vize audit completed successfully.")

if __name__ == "__main__":
    auditor = VizeVaultwardenAuditor()
    # Complex instruction set: mov eax, 0x1234 -> nop -> sub rsp, 8
    auditor.audit_binary_code("b834120000904883ec08")
    auditor.audit_supply_chain()
    auditor.audit_forensic_leftovers()
