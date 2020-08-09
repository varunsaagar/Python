name = "Varun"
def home():
    name ="Dood"
    def bro():
        nonlocal name
        name = "saagar"

    print("Value %s" % name)
    bro()
    #print("Value %s" % name)
home()
print(globals())
print(locals())

#print(name)
