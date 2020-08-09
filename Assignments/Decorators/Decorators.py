# def div (a,b):
#     print(a/b)
# div(2,4)
#
# def div (a,b):
#     if a<b:
#         a,b = b,a
#     print(a/b)
#
# div(2,4)

def div (a,b):
    print (a/b)

def smart_dic(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func (a , b)
    return inner

div1=smart_dic(div)
div1(2,4)

#print(div)