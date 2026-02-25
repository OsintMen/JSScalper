# utils/logger.py

import sys

# ANSI color codes
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

def info(message):
    print(f"{BLUE}[INFO]{RESET} {message}")

def warning(message):
    print(f"{YELLOW}[WARN]{RESET} {message}")

def success(message):
    print(f"{GREEN}[SUCCESS]{RESET} {message}")

def error(message):
    print(f"{RED}[ERROR]{RESET} {message}")
    sys.exit(1)