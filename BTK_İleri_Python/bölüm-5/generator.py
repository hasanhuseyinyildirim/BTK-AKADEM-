
def counter(max):
    sayi=1
   # sayilar=[]

    while sayi<=max:
       # sayilar.append(sayi)
        yield sayi
        sayi+=1
    #return sayilar

# sonuc=counter(20)

sonuc=list(counter(20))

print(sonuc)
#print(next(sonuc))