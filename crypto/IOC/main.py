# INIT
#alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
data = []
freq = {}

# File - Load Function
def load(file):
    handle = open(file)
    return handle.read()

# Text Format
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
    format = format.replace('(','')
    format = format.replace(')','')
    format = format.replace('"','')
    format = format.replace('?','')
    format = format.replace("'",'')
    format = format.replace(':','')
    format = format.upper()
    return format

def FREQ(message,list_):
    for i in message:
        list_[i]=list_.get(i,0)+1
    for i in sorted(list_):
        print((i, list_[i]), end =" ")

def COUNTER(message,list_):
    for letters in message:
        list_.append(letters)
    length = (len(list_))
    return length

form('File1.txt')
message = form(input('File: '))

print(COUNTER(message,data))
FREQ(message,data)