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
        