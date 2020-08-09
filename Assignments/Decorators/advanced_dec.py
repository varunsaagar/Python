from functools import wraps

def exp_number(num):
    def calculate_exp(func):
        @wraps(func)
        def square_wrapper(x,y):
            return [z**num for z in func(x,y)]
        return square_wrapper
    return calculate_exp

@exp_number(3)
def return_lst(x,y):
    return range(x+1, y)

#
#def add_num():
#     print("nothing")
#
print(return_lst.__name__)

print(return_lst(1,5))

