#init
bits = []

#File Load Function
def load(file):
    handle = open(file)
    for bit in handle:
        bits.append(bit)

load('project2part2ciphertext.txt')
print(bits)
