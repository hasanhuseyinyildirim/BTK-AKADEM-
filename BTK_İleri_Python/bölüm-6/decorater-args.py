# def dec_selamlama(count):
#     def selamlama(fn):
#             def inner(isim):
#                 for _ in range(count):
#                     fn(isim)
#             return inner
#     return selamlama


# @dec_selamlama(count=2)
# def gunaydin(isim):
#     print(f"günaydın benim adım {isim}")

# @dec_selamlama(count=3)
# def iyigunler(isim):
#     print(f"iyi günler benim adım {isim}")


# gunaydin("Hasan")
# iyigunler("Hüseyin")


import time
def dec_speed_test(count):
    def speed_test(fn):
        def inner(*args,**kwargs):
            start_time=time.time() #start_time=time.perf_counter
            print(f"{fn.__name__} metotu çalışıyor.")
            for _ in range (count):
                result=fn(*args,**kwargs)
                end_time=time.time() #end_time=time.perf_counter
                run_time=end_time - start_time
                print(f"geçen süre {run_time}")
            return result
        return inner
    return speed_test
        

@dec_speed_test(count=2)
def sum_gen():
    return sum((x for x in range(10000000)))

@dec_speed_test(count=3)
def sum_list():
    return sum([x for x in range(10000000)])

print(sum_gen())

print(sum_list())