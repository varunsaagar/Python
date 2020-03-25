string1 = {'A':'DO WITH LOVE'}
string2 = {'B':'EVERY MOMENT WILL BE HAPPIEST ONE'}
string1.update(string2) #Using fuction i can combine -Type 1
print(string1)
string= {**string1, **string2}
print (string) #Using Optrations & value assignment i can combined - type 2
for x,y in string1.items(): #Just printed only str without any special charcters

    print(y)

