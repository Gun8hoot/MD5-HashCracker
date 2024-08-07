import time, os 

def writerep(given_hash, word):
    path_linux = "report/"
    path_win = 'report\\'
    try:
        if os.name == 'nt':
            os.makedirs(path_win)
        else:
            os.makedirs(path_linux)
    except FileExistsError:
        pass


    rp_name = f"{word}:" + time.strftime('%d-%m-%Y')+ "_report-crackers.txt"
    if os.name == 'nt':
        create_report = open(path_win + rp_name, "w")
        write_report = create_report.writelines(f"{given_hash} : {word}")
        print(f'\n[+] A report was create in {path_win}{rp_name}')
    else:
        create_report = open(path_linux + rp_name, "w")
        write_report = create_report.writelines(f"{given_hash} : {word}")  
        print(f'\n[+] A report was create in ./{path_linux}{rp_name}')