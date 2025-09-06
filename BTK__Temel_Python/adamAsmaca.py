import random
Liste=["python","print","random","choice"]
kelime=random.choice(Liste)
adam=['''
    +----+
    o    |
   /|\\   |
   / \\   |
        ---''','''
    +----+
    o    |
   /|\\   |
   /     |
        ---''','''
    +----+
    o    |
   /|\\   |
         |
        ---''','''
    +----+
    o    |
   /|    |
         |
        ---''','''
    +----+
    o    |
    |    |
         |
        ---''','''
    +----+
    o    |
         |
         |
        ---''','''
    +----+
         |
         |
         |
        ---''']


dogruHarf=[]
yanlisHarf=[]
hak=len(adam)

while hak>0:
    out=""
    for h in kelime:
        if h in dogruHarf:
            out+=h
        else:
            out+="_"
    if out == kelime:
        break
    print("kelime",out)
    print(adam[hak-1])
    girHarf=input()
    if girHarf in dogruHarf or girHarf in yanlisHarf:
        print(girHarf,"Zaren girildi")
    elif girHarf in kelime:
        print("doğru harf")
        dogruHarf.append(girHarf)
    else:
        print("yanlış harf")
        hak-=1
        yanlisHarf.append(girHarf)

if hak !=0:
    print("Kazandınız.. Kelimeniz..: ",kelime)
else:
    print("Maalesef.. Kaybettiniz.. Kelimeniz..:",kelime,"idi")

    