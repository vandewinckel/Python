# INIT
data = []
numeric = []
normal = []

# File - Load Function
def load(file):
    handle = open(file)
    return handle.read()

# Text Format
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
    return format

    #ADDS TO LIST
    for letter in format:
        data.append(letter)

    #REMOVE NUM
    for letter in data:
        global numbers
        numbers = ""
        
        if not letter.isdigit():
            normal.append(letter)
        else:
            numeric.append(letter)
            numbers = ''.join(numeric)
            
    return format, numbers
