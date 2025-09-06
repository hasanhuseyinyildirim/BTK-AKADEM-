#iterable
#iterator

sayilar=[1,2,3,4,5]

iterator = iter(sayilar)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

while True:
    try:
        sayi=next(iterator)
        print(sayi)
    except StopIteration:
        break
