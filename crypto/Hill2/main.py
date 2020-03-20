import numpy as np

def breaker(line):
    array = [line[i:i+4] for i in range(0, len(line), 4)]
    for word in array:
        if len(word) < 4:
            temp = word
            array.remove(word)
            temp += 'X'*(4 - len(temp))
            array.append(temp)
    print(array)
    return array

def packer(list):
  return "".join(list)

packer(breaker('HELLOWORLD')
