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


cheie = sys.argv[1]
fisier_input = sys.argv[2]
fisier_output = sys.argv[3]

# citeste fisier input
f = open(fisier_input, "r")
text = f.read()

message = text.encode('utf8')

# converteste in ascii
text_con = convert(message)
cheie_con = convert(cheie)

# text_con ^ cheie_con
criptat = cripty(text_con, cheie_con)

# scrie ca bytes
f = open(fisier_output, "wb")
f.write(bytes(criptat))
f.close()