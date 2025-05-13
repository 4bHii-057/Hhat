import sys
import traceback

try:
    import payal
except Exception as e:
    print("[!] Error importing .so:", e)
    traceback.print_exc()
    sys.exit(1)
# Your encrypted module is now running.
