import hashlib as hl
import time
import os

class hash_entity:
    def __init__(self, file_name, timestamp, hash_value):
        self.file = file_name
        self.time = timestamp
        self.hash = hash_value

def comp_hash(file):
    BLOCK_SIZE = 65536
    alg = hl.md5()
    with open(file, 'rb') as f:
        file = f.read(BLOCK_SIZE)
        while len(file) > 0:
            alg.update(file)
            file = f.read(BLOCK_SIZE)
        f.close()
    return str('['+str(time.asctime(time.localtime()))+'] | '+alg.hexdigest())

def hash_path(path):
    with os.scandir(path) as dir:
        for item in dir:
            try:
                return str(item.name+' | '+comp_hash(item.path))
            except:
                pass

def hash_file(path,fname):
    with os.scandir(path) as dir:
        for item in dir:
            if str(item.name) == fname:
                return str(item.name+' | '+comp_hash(item.path))
            else:
                print('File Name not found: ', str(item))