#Sortear a palavra
import random
#JOGO DA FORCA
topo = "UU=====U"
corda = "||    |"
cabeca ="||     "
corpo = "||     "
pernas ="||     "
base1="||"
base2="||"
dica=""
#é necessário criar uma váriavel para cada letra
l1=l2=l3=l4=l5=l6=l7=l8=l9="_"
palpites=""
erro=acerto=0
palavras=["BATRANGUE", "AEROPORTO", "CONSELHOS"]
dicas=["Morcego que vai e volta",
       "Local onde podemos viajar",
       "Se fossem bons, não eram de graça"]
#Sorteando a palavra
sorteio=random.randint(0,2)
sorteado=palavras[sorteio]
palavra=[]
for i in range(0,9,1):
    palavra.append(sorteado[i:i+1]) #Separa a palavra dentro de uma lista
dica=dicas[sorteio]
while (acerto < 9 and erro <6):
    #Exibindo a forca
    print()
    print()
    print(dica)
    print()
    print(topo)
    print(corda)
    print(cabeca)
    print(corpo)
    print(pernas)
    print(base1)
    print(base2)
    print(" ",l1,l2,l3,l4,l5,l6,l7,l8,l9)
    print()
    print(palpites)
    print()
    print("Digite uma letra")
    letra=input().upper()
    print()
    print()
    print()
    palpites += " " + letra
    #TESTANDO E ACERTOU OU ERROU
    if letra in palavra : #Se a letra que ele digitou esta contida na lista...
        if letra == palavra[0]:
            l1=letra
            palavra[0] = "@"
            acerto +=1
        if letra == palavra[1]:
            l2=letra
            palavra[1] = "@"
            acerto +=1
        if letra == palavra[2]:
            l3=letra
            palavra[2] = "@"
            acerto +=1
        if letra == palavra[3]:
            l4=letra
            palavra[3] = "@"
            acerto +=1
        if letra == palavra[4]:
            l5=letra
            palavra[4] = "@"
            acerto +=1
        if letra == palavra[5]:
            l6=letra
            palavra[5] = "@"
            acerto +=1
        if letra == palavra[6]:
            l7=letra
            palavra[6] = "@"
            acerto +=1
        if letra == palavra[7]:
            l8=letra
            palavra[7] = "@"
            acerto +=1
        if letra == palavra[8]:
            l9=letra
            palavra[8] = "@"
            acerto +=1
    else:
        erro += 1
    #ARRUMANDO A FORCA
    if erro == 1:
        cabeca ="||  (Ï)"
    elif erro == 2 :
        corpo = "||  {.}"
    elif erro== 3 :
        corpo = "||  /{.}"
    elif erro == 4:
        corpo = "||  /{.}\\"
    elif erro == 5 :
        pernas ="||   L  "
    elif erro ==6:
        pernas ="||    LL"
#Exibindo a forca final fora da estratura de repetição
print()
print()
print(dica)
print()
print(topo)
print(corda)
print(cabeca)
print(corpo)
print(pernas)
print(base1)
print(base2)
print(" ",l1,l2,l3,l4,l5,l6,l7,l8,l9)
print()
print(palpites)
print()
if acerto >= 9:
    print("VOCÊ ACERTOU!!")
else :
    print("VOCÊ PERDEU!!")