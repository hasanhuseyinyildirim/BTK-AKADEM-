# def selam(isim):
#     return f"selam, {isim}"

# print(selam("çınar"))
# print(selam)

# merhaba=selam

# print(selam)
# print(merhaba)

# del selam
# print(merhaba)

# # print(selam("çınar"))
# print(merhaba("Çınar"))



# def outer(number):
#     def inner(number):
#         print(number)
#     inner(number)
# outer(10)

def faktoriyel(sayi):
    if sayi <=1:
        return 1
    
    return sayi*faktoriyel(sayi-1)

sonuc=faktoriyel(5)
print(sonuc)

sonuc=faktoriyel(15)
print(sonuc)