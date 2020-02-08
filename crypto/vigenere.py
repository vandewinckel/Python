alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

indexedLetter = dict(zip(alphabet, range(len(alphabet))))
letteredIndex = dict(zip(range(len(alphabet)),alphabet))

# File - Load Function
def load(file):
    handle = open(file)
    return handle.read()
    
# Format
def form(file):
    format = load(file)
    format = ''.join([i for i in format if not i.isdigit()])
    format = format.replace(' ', '')
    format = format.replace(',', '')
    format = format.replace('-', '')
    format = format.replace('–', '')
    format = format.replace('—', '')
    format = format.replace('.', '')
    format = format.replace(';', '')
    format = format.replace('\n', '')
    format = format.upper()
    format = str(format)
    return format
    
# Encryption 
def encrypt(plaintext,key):
    encrypted = ''
    split_plaintext = [plaintext[i:i + len(key)] for i in range(0, len(plaintext), len(key))] #(start, end, step)
    for each_split in split_plaintext:
        i = 0
        for letter in each_split:
            number = (indexedLetter[letter] + indexedLetter[key[i]]) % len(alphabet) #adding indexed letter from key
            encrypted += letteredIndex[number]
            i+=1
    return encrypted

# Decryption
def decrypt(cipher,key):
    decrypted = ''
    split_cipher = [cipher[i:i + len(key)] for i in range(0, len(cipher), len(key))] #(start, end, step)
    for each_split in split_cipher:
        i = 0
        for letter in each_split:
            number = (indexedLetter[letter] - indexedLetter[key[i]]) % len(alphabet) #sub indexed letter from key
            decrypted += letteredIndex[number]
            i+=1
    return decrypted

def main():

    message = form(input("Enter File Name: "))
    key = input("Enter Key: ")
    
    select_process = input("Enter [Encrypt : Decrypt]: ")
    select_process = select_process.strip()
    select_process = select_process.title()
    
    if select_process == 'Encrypt':
        print(encrypt(message, key))
    elif select_process == 'Decrypt':
        print(decrypt(message, key))
    else:
        print('Nah fam, enter that good input: ')

main()
