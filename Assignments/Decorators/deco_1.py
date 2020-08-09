import time


def calculate_time(func):
    def time_wrapper(x,y):
        start = time.time()
        print(func(x,y))
        end = time.time()
        return (end-start)*10000
    return time_wrapper

@calculate_time
def add_num(x,y):
    return x+y

@calculate_time

def subtract_numbers(x,y):
    return x-y

#result = calculate_time(add_num)
print(add_num(10,24))
print(subtract_numbers(10,3))