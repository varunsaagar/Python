import time

def time_it(func):
    def wrapper (*args ,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end= time.time()
        print(func.__name__ + 'taken time ' + str((end - start) * 1000) + "mill sec")
        return result
    return wrapper

@time_it
def cal_sq(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def cal_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result

arras= range(1,10)
output_sq = cal_sq(arras)
output_sq = cal_cube(arras)