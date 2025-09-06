# 1
liste = [sayi for sayi in range(1,101) if sayi % 12 ==0]
print(liste)

# 2
text = "Hello 12345 World"
sayiListe = [int(i) for i in text if i.isdigit()]
print(sayiListe)

# 3

sicakliklar = [20,15,0,-5,-2]
sonuc = [i if i>=4  else "Buzlanma Tehlikesi"  for i in sicakliklar ]
print(sonuc)

# 4

ogrenciler=["ali","ahmet","canan"]
notlar=[50,60,80]

notListe = [(ogrenciler[i],notlar[i]) for i in range(0,len(ogrenciler))]
liste_dict = {key:value for (key,value) in notListe if value > 50}

print(liste_dict)
