alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

indexedLetter = dict(zip(alphabet, range(len(alphabet))))
letteredIndex = dict(zip(range(len(alphabet)),alphabet))

# File - Load Function
def load(file):
    handle = open(file)
    return handle.read()
#Formatter
def form(file):
    format = load(file)
    format = format.replace(' ', '')
    format = format.replace(',', '')
    format = format.replace('-', '')
    format = format.replace('–', '')
    format = format.replace('—', '')
    format = format.replace('.', '')
    format = format.replace(';', '')
    format = format.replace('\n', '')
    format = format.upper()

#Encryption 
def encrypt(plaintext,key):
    encrypted = ''
    split_plaintext = [plaintext[i:i + len(key)] for i in range(0, len(plaintext), len(key))]
    for each_split in split_plaintext:
        i = 0
        for letter in each_split:
            number = (indexedLetter[letter] + indexedLetter[key[i]]) % len(alphabet)
            encrypted += letteredIndex[number]
            i+=1
    return encrypted

def main():
    #message = form('project2plaintext.txt.txt')
    print(indexedLetter)

main()