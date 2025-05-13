import os
import sys
import payal  # make sure this module exists and is in the PYTHONPATH

# Auto-executed main block
print("[*] Enter full path to .py file to encrypt:")
path = input(">> ").strip()

if not os.path.isfile(path):
    print("[-] Invalid file path")
    sys.exit(1)

filename = os.path.basename(path)

# Assuming build_so is a function inside payal module
payal.build_so(path, filename)
