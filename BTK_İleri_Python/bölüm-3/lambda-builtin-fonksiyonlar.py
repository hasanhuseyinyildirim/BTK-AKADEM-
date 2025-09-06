sayilar = [1,2,3,4,5]
# kareleri=[]

# for sayi in sayilar:
#     kareleri.append(sayi**2)

# print(kareleri)

# def kareAl(sayi):
#     return sayi**2

# sonuc = list(map(lambda sayi:sayi**2,sayilar))
# print(sonuc)


# kurslar =[
#     {"title":"python","count":10000},
#     {"title":"python","count":20000},
#     {"title":"javascript","count":5000}
# ]

# sonuc = sorted(kurslar,key=lambda kurs:kurs["count"])
# sonuc = sorted(kurslar,key=lambda kurs:kurs["count"],reverse=True)
# sonuc = list(map(lambda kurs:kurs["title"],sorted(kurslar,key=lambda kurs:kurs["count"],reverse=True)))
# print(sonuc)


# isimler=["ahmet","ali","ada","yiğit"]

# sonuc=min(isimler)
# sonuc=max(isimler)
# sonuc=min(len(isim) for isim in isimler)
# sonuc=max(len(isim) for isim in isimler)
# sonuc=min(isimler,key=lambda isim:len(isim))
# sonuc=max(isimler,key=lambda isim:len(isim))
# print(sonuc)


# urunler =[
#     {"title":"samsung s23","price":70000},
#     {"title":"samsung s24","price":80000},
#     {"title":"samsung s25","price":90000}
# ]

# sonuc=min(urunler,key=lambda urun:urun["price"])
# sonuc=max(urunler,key=lambda urun:urun["price"])["title"]

products = [
    {"title":"iphone 15","price":60000},
    {"title":"iphone 16","price":70000},
    {"title":"iphone 17","price":80000},
    {"title":"iphone 18","price":0}
]

toplamFiyat=sum([urun["price"] for urun in products])
urunAdeti=len([urun for urun in products if urun["price"]>0])
sonuc = toplamFiyat/urunAdeti

print(sonuc)
