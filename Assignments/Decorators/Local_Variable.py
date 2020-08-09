def number ():
    x= 100
    def add():
        print(x)
    return add

result = number()
result()