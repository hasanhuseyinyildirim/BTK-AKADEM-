import time

def speed_test(fn):
    def inner(*args,**kwargs):
        start_time=time.time() #start_time=time.perf_counter
        print(f"{fn.__name__} metotu çalışıyor.")
        result=fn(*args,**kwargs)
        end_time=time.time() #end_time=time.perf_counter
        run_time=end_time - start_time
        print(f"geçen süre {run_time}")
        return result
    return inner
        

@speed_test
def sum_gen():
    return sum((x for x in range(10000000)))

@speed_test
def sum_list():
    return sum([x for x in range(10000000)])

print(sum_gen())

print(sum_list())