import payal

if hasattr(payal, "main"):
    payal.main()
else:
    print("[!] Error: 'main' function not found in payal module.")
    print("Available functions/attributes:", dir(payal))
