import sys
import wsgiref.validate


def convert(t):
    newt = []
    for i in range(len(t)):
        if isinstance(t[i], str) :
            newt.append(ord(t[i]))
        else :
            newt.append(int(t[i]))
    return newt

def reconvert(t):
    s = ""
    s = "".join(t)
    return s


fisier_input = sys.argv[1]
fisier_output = sys.argv[2]

# citeste ca bytes
f = open(fisier_input, "rb")
text = f.read()

# converteste in ascii
text_con = convert(text)

g = open(fisier_output, "w")


solutie=[[]]*6
lg=len(text_con)
caracteretext="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890, (){}[].-!?:;\n\t\v\"\'\r\f"
caractere="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
for k in range(10,16):
    for i in range(k):
        for j in caractere:
            ci=i
            while ci<lg:
                if caracteretext.find(chr(text_con[ci]^ord(j)))==-1:
                    break
                ci = ci+k
            if ci>=lg:
                solutie[k-10].append(j)
                break
    if len(solutie[k-10]) == k:
        g.write(reconvert(solutie[k-10]))
        break