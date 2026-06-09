# Frida Environment Crash Log
Execution of `src/frida_manager.py` initially failed with `ModuleNotFoundError: No module named 'frida'`.
Mitigation: Enforced root library resolution via `pip3 install -r requirements.txt --break-system-packages` to bypass PEP 668 restrictions on Kali Linux.
