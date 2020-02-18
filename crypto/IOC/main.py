# INIT
#alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
data = []
iocl = []

freq = {}   #working freq dict
letFreq = []    #using freq list


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

def FREQ(message,dic,output): #Takes message and dictionary [FREQ] and computes letter frequency
    for i in message:
        dic[i]=dic.get(i,0)+1
    for i in sorted(dic):
        output.append(dict(letter = i, frequency = dic[i]))

def COUNTER(message,list_): #Takes message and list [data] to compute letter count
    for letters in message:
        list_.append(letters)
    length = (len(list_))
    return length

def ioc(lst):
    for i in range(26):
        iocl.append(lst[i]['frequency'] * (lst[i]['frequency']-1))
    IOC = sum(iocl)
    return IOC

def main():
    message = form(input('File: ')) #Load and format input text file
    print("Number of Character in DATA:", COUNTER(message,data))
    FREQ(message,freq,letFreq)
    print(ioc(letFreq))

main()