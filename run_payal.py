# run_payal.py

import payal  # ye aapka .so file hai jo import hoga

# Agar usme koi specific function hai jaise: main() ya start()
# toh usko call karo. For example:
try:
    payal.main()
except Exception as e:
    print("[!] Error:", e)
