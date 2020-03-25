L=[1,2,3,4,5,6]
print (L)
print ('Address {}'.format(id(L)))  #ADDRESS OF THE INT
L[2]=9 #CHANGE IN INT FROM POSTION 2
print(L)
print ('Address {}'.format(id(L))) #ADDRESS OF THE CHANGED INT IS SAME AS BEFORE