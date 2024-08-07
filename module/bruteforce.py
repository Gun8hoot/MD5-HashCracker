import time, string, os, sys, itertools
import hashlib
from module.writereport import writerep
from module.color import color

# Banner
if os.name == 'nt':
    with open('assets/banner_win.txt', 'r') as f:
        banner = f.read()
elif os.name != 'nt':
    with open('assets/banner_unix.txt', 'r') as f:
        banner = f.read()



def brutef_attack(raw_hash):
    # Main script
    result = bruteforcenow(raw_hash)

    # Result of the operation
    if result:
        print ("\033[A                                                               \033[A")
        print(color.fr_red + f"[+] {raw_hash} : {result}" + color.reset)
        writerep(raw_hash, result)
    else:
        print(color.fr_red + "[!] ERROR" + color.reset)
        sys.exit()
        
        
def bruteforcenow(enc_hash):
    # Vars
    max_length = 30
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # Generate character
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            guess_hash = hashlib.md5(guess.encode()).hexdigest()
            print(guess_hash, ':', guess)
            print ("\033[A                             \033[A")
            if guess_hash == enc_hash:
                return guess
