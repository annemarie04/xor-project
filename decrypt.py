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



cheie = sys.argv[2]
fisier_input = sys.argv[1]
fisier_output = sys.argv[3]

# citeste ca bytes
f = open(fisier_input, "rb")
text = f.read()

# converteste in ascii
text_con = convert(text)
cheie_con = convert(cheie)

# text_con ^ cheie_con
criptat = cripty(text_con, cheie_con)

# afiseza text
f = open(fisier_output, "w")
f.write(bytes(criptat).decode('utf8'))
f.close()