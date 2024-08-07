import time, string, os, sys, subprocess, hashlib, string
from module.writereport import writerep
from module.color import color

def wordlist_check(PathWL):
    if PathWL == None:
        wl_choise = input(f"{color.fr_red}[!] It seems you don't do a dictionary bruteforce attack, but you don't specify a path for the wordlist. Do you want to use build in rockyou wordlist ? (Y/N)\n{color.reset}")
        print ("\033[A                             \033[A")
        if wl_choise == "N" or wl_choise == "n":
            sys.exit(0)
        elif wl_choise == "Y" or wl_choise == "y":
            try:
                rk_txt = subprocess.Popen('gzip -d ./rockyou.txt.gz', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  #TODO
                for line in rk_txt.stdout.readlines():
                    print(line)
                return 'rockyou.txt.gz'
            except (FileNotFoundError, NotADirectoryError):
                print("[!] ERROR")
                sys.exit(0)
    else:
        pass

def dict_attack(hash, PathWL):
    wordlist_check(PathWL)
    if PathWL == None:
        PathWL = wordlist_check(PathWL)
    elif PathWL != None:
        with open(str(PathWL)) as f:
            WL = f.readlines()

        # Hash Cracking Loop
        try:
            count = 0
            for lines in WL:
                count += 1
                ml = lines.replace('\n', '')
                m = hashlib.md5()
                m.update(ml.encode())
                pipe = m.hexdigest()
                print ("\033[A  \033[A")
                print(f"[+] Number of attempt {count} : Time spend ")

                if pipe == hash:
                    writerep(pipe, ml)
                    print(color.fr_green + f'[!] Hash password found ! {hash}:{ml}' + color.reset)
                    result = pipe + " : " + hash
                    return result
                else:
                    pass
        except KeyboardInterrupt:
            print('[!]KEyBoaRD')