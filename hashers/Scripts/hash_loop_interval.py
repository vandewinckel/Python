import os, sys, time
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import lib.file_hash as hf

clear = lambda: os.system('cls')

def full_dir():
    clear()
    active = True
    path = input('Enter Path of Dir: ')
    t2h = input('<int> Enter Interval of Hashing: ')
    print('')
    while active:
        print(hf.hash_path(path))
        time.sleep(int(t2h))

full_dir()