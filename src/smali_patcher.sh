#!/bin/bash
# Module: APKTool & Smali Orchestration Lab
# Course: Reverse Engineering (BGT210)
# Description: Automates Decompile -> Patch -> Rebuild -> Sign pipeline.

echo -e "\e[1;36m\n[*] Phase 12: Smali Orchestration Pipeline Initialized\e[0m"
mkdir -p workspace/smali/com/target/

# 1. Simulating Decompilation (Creating a mock Smali file)
echo -e "\e[34m[*] Simulating APKTool Decompile...\e[0m"
cat << 'SMALI' > workspace/smali/com/target/LicenseChecker.smali
.class public Lcom/target/LicenseChecker;
.super Ljava/lang/Object;

.method public isPremium()Z
    .registers 2
    # Original logic: return false
    const/4 v0, 0x0
    return v0
.end method
SMALI

echo -e "\e[32m  [+] Original Smali logic created: isPremium() returns 0x0 (False)\e[0m"

# 2. Patching the Smali file
echo -e "\e[34m\n[*] Applying targeted Smali patch (Boolean True Bypass)...\e[0m"
# Changing 0x0 to 0x1 using stream editor
sed -i 's/const\/4 v0, 0x0/const\/4 v0, 0x1/g' workspace/smali/com/target/LicenseChecker.smali

echo -e "\e[31m  [!] Patch applied successfully! isPremium() now returns 0x1 (True)\e[0m"

# 3. Simulating Rebuild & Sign
echo -e "\e[34m\n[*] Simulating APKTool Build & apksigner...\e[0m"
echo -e "\e[32m  [+] Recompiled and Signed APK successfully generated at workspace/target_patched.apk\e[0m"
echo -e "\e[1;35m[*] Orchestration complete.\n\e[0m"
