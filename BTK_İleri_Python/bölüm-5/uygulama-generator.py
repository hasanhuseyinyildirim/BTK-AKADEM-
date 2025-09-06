#(1-sonsuz) aralığında her sayının karesini getiren fonksiyon

# def sayi_uret():
#     sayi=0
#     while True:
#         yield sayi**2
#         sayi+=1
    

# generator = sayi_uret()

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


#fibonacci serisi üreten hem normal fonksiyon hem generator 

# normal fonksiyon
# def fib_list(max):
#     sayilar=[]

#     a,b=0,1

#     while len(sayilar) < max:
#         sayilar.append(b)
#         a,b=b,a+b

#     return sayilar

# sonuc=fib_list(9000)

# print(sonuc)


# generator

# def fib_gen(max):
#     a,b=0,1
#     count=0
#     while count<=max:
#         a,b=b,a+b
#         yield b


# for i in fib_gen(9000):
#     print(i)


# generator ve listenin bellekteki kapladığı alanlar ve işlem süreleri karşılaştırması


# import sys

# liste =[i for i in range(10000)]
# print(sys.getsizeof(liste))

# gen =(i for i in range(10000))
# print(sys.getsizeof(gen))


import time

list_start_time=time.time()
sum([i for i in range(9000000)])
list_stop=time.time()-list_start_time
print(list_stop)

gen_start_time=time.time()
sum((i for i in range(9000000)))
gen_stop=time.time()-gen_start_time
print(gen_stop)