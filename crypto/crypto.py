#init

#Fie Load Function
def load(file):
    handle = open(file)
    return handle.read()

#Text format
def form(file):
    ptext = load(file)
    sptext = ptext.replace(' ', '')
    sptext = sptext.replace(',', '')
    sptext = sptext.replace('-', '')
    sptext = sptext.replace('–', '')
    sptext = sptext.replace('—', '')
    sptext = sptext.replace('.', '')
    sptext = sptext.replace(';', '')
    sptext = sptext.replace('\n', '')
    return sptext

#print(form('project2plaintext.txt.txt'))

#Index Numbers
def indx(file):
    load(file)