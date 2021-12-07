import sys

def convert(t):
    newt = []
    for i in range(len(t)):
        if isinstance(t[i], str) :
            newt.append(ord(t[i]))
        else :
            newt.append(int(t[i]))
    return newt

def cripty(message, key):
    for i in range(len(message)):
        k = key[i % len(key)]
        message[i] = message[i] ^ k
    return message

f = open(sys.argv[1], "r")
g = open(sys.argv[2], "rb")
h = open(sys.argv[3], "w")
a = f.read()
b = g.read()
for c in range(10, 16):
    mesaj = []
    mesaj = cripty(convert(a[:c]), convert(b[:c]))
    #print(mesaj)
    h.write(bytes(mesaj).decode('utf8')+'\n')
f.close()
g.close()
h.close()




