# Smali Editing & Patching Guide

## Introduction
This guide outlines the standard operating procedure for modifying Dalvik bytecode (Smali) to bypass client-side restrictions.

## Boolean Return Patching
When bypassing license checks or premium feature locks, the goal is often to force a method to return `true` instead of `false`.

**Original Smali (Returns False):**
`const/4 v0, 0x0`
`return v0`

**Patched Smali (Returns True):**
`const/4 v0, 0x1`
`return v0`

## Orchestration Pipeline
The `src/smali_patcher.sh` script automates this process using standard CLI tools like `sed` to intercept and replace opcode variables dynamically before recompilation via APKTool.
