import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import lib.file_hash as hf

clear = lambda: os.system('cls')

def full_dir():
    clear()
    path = input('Enter Path of Dir: ')
    print('')
    print(hf.hash_path(path))
    print('')
    input('Press any Enter to continue...')

full_dir()