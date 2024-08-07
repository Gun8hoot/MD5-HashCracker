#!/bin/env python3

# Import module
from module.color import *
import os,sys,argparse

# Banner
if os.name == 'nt':
    with open('assets/banner_win.txt', 'r') as f:
        banner = f.read()
elif os.name != 'nt':
    with open('assets/banner_unix.txt', 'r') as f:
        banner = f.read()

# ARGUMENTS
parser =argparse.ArgumentParser(prog='HASH CRACKERS', description='MD5 hashes crackers write in python (bruteforce & dictionary attack available)')
parser.add_argument('-hash', '--hash', dest='HASH')
parser.add_argument('-w', '--wordlist', dest='WORDLIST')
parser.add_argument('-tp', '--type', dest='TYPE')
args = parser.parse_args()
# ---
HASH = args.HASH
WORDLIST = args.WORDLIST
TYPE = args.TYPE

# FUNCTION
def main():
    try:
        print(color.fr_green + banner + color.reset)
        if TYPE == 'bruteforce':
            from module.bruteforce import brutef_attack
            brutef_attack(HASH)
        elif TYPE == 'dictionary':
            from module.dictionary import dict_attack
            dict_attack(HASH, WORDLIST)
        elif TYPE == None:
            print(f"{color.fr_red}[!] You need to choose an attack !{color.fr_orange}\n 2 available: bruteforce, dictionary{color.reset}")
            sys.exit(0)
    except KeyboardInterrupt:
        print("\n[!] Keyboard interrupt keys press")
        sys.exit(0)


# EXEC
if __name__ == '__main__':
    main()