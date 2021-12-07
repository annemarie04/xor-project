Use:

python encrypt *cheiesecreta* input.txt output
<br>
python decrypt output *cheiescreta* input_recuperat.txt

Partea1:
python partea1 input output parole.txt

Partea2:
python partea2 output parole.txt

Echipa noastra: gcodes
Echipa adversa: 404NameNotFound
Cheia echipei adverse:   Rebreanu1920


!!!IMPORTANT!!!: La rularea programului de encrypt al echipei adverse ne rezulta un output care continea unele caractere NUL, care
nu existau cand copiam output-ul de pe git. Noi am lucrat cu output-ul rezultat din rularea codului lor.

Prima parte: 

Am observat ca pentru a ajunge la parola ne putem folosi de sirurile de caractere din input-ul, 
respectiv output-ul echipei adverse. Dupa conversia fiecarui fisier in cod ASCII (input_convertit, respectiv output_convertit),
am aplicat urmatorea echivalenta:
input xor cheie = output <=> input xor cheie xor output = 0 <=> cheie xor input xor output = 0 <=> cheie = input xor output.
Parola fiind alcatuita dintr-un numar de 10-15 caractere, am considerat importante numai primele 15 caractere din fisierele
echipei adverse. Pe rand, xorand primele 10 elemente din input_convertit si output_convertit(input_convertit[0] xor output_convertit[0], 
input_convertit[1] xor output_convertit[1], .... , input_convertit[9] xor output_convertit[9]) si apoi convertind aceste coduri ascii 
in caractere, a rezultat o posibila parola. Analog, am procedat pentru primele 11 elemente din input_convertit si output_convertit,
apoi pentru primele 12 elemente din input_convertit si output_convertit ..... pentru 
primele 15 elemente din input_convertit si output_convertit.
Astfel, ne-au rezultat 6 posibile parole, dintre care, una trebuia sa fie parola corecta.
Am rulat codul de encrypt al echipei adverse pentru fiecare posibila parola si de fiecare data am comparat
output-ul rezultat cu output-ul echipei adverse. Cand am descoperit ca cele 2 output-uri coincid, 
am fost siguri de veridicitatea raspunsului, anume, Rebreanu1920. (Plus ca inputul lor era un fragment din opera literara "Ion", publicata 
de Liviu Rebreanu in anul 1920).


A doua parte:
Pentru a aflat cheia folosindu-ne doar de output, am generat pe rand, strategic, posibilitati de chei pana cand una dintre acestea, xorata
cu outputul rezulta un input valid (sa contina doar litere, cifre, semne de punctuatie si caractere)
Am utilizat faptul ca:
output_convertit xor cheie_posibila_convertita = input_valid_convertit => cheie = cheie_posibila

Cum am generat cheile posibile:
Am abortat o solutie bruta: am considerat, pe rand, lungimile posibile de parola si pentru fiecare am generat parolele 
dupa urmatorul procedeu:
Cautam intai primul caracter al parolei, acesta luand valori din multimea literelor latine si cea a cifrelor. 
Xoram codul ASCII al lui cu coduri ASCII ale caracterelor din output aflate la distanta de lungimea parolei una de alta
pana cand rezultatul contine un caracter ce nu ar putea apartine textului initial. 
Daca nu conduce la niciun caracter invalid, atunci ii atribuim pozitiei din parola acel caracter pe care-l verificam.
In caz contrar, trecem la urmatorul caracter de verificat pentru acea pozitie din parola.



