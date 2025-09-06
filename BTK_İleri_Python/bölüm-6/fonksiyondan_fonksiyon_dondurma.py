def usAlma(taban):
    def inner(us):
        return taban**us
    return inner



# sonuc=usAlma(2)(5)
# print(sonuc)
# fn=usAlma(5)
# sonuc=fn(3)

# print(sonuc)


def yetki_sorgulama(sayfa):
    def inner(role):
        if role =="Admin":
            return f"{role} rolü {sayfa} sayfasına ulaşabilir"
        else:
            return f"{role} rolü {sayfa} sayfasına ulaşamaz"
    return inner


# yetki = yetki_sorgulama("Ürün Güncelleme")
# sonuc =yetki("Admin")
# print(sonuc)

def islem(islem_adi):
    def toplama(*args):
        result_topl=0
        for i in args:
            result_topl+=i
        return result_topl

    def carpma(*args):
        result_carp=1
        for i in args:
            result_carp*=i
        return result_carp
    
    if islem_adi=="toplama":
        return toplama
    else:
        return carpma


toplama=islem("toplama")
carpma=islem("carpma")


sonuc=toplama(10,20)
print(sonuc)

sonuc=carpma(10,20)
print(sonuc)