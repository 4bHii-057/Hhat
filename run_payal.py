import payal
# Auto-executed main block
print("[*] Enter full path to .py file to encrypt:")
path = input(">> ").strip()
if not os.path.isfile(path):
print("[-] Invalid file path")
sys.exit(1)
filename = os.path.basename(path)
build_so(path, filename)
