def filter(fn,liste):
    result = []
    for item in liste:
        if fn(item):
            result.append(item)
    return result

def is_even(sayi):
    return sayi % 2 == 0

def is_positive(sayi):
    return sayi >0



sayilar=[1,2,3,4,5,8,-5,-7,-15,95,26,-36,0]
sonuc = filter(is_even,sayilar)
sonuc=filter(is_positive,sayilar)


print(sonuc)