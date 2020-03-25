L=('a','b','c','d')
print (L)
print ('Address {}'.format(id(L))) #ADDRESS OF THE INT

L(2)='v' #CHANGE IN INT FROM POSITION 2
print(L)
print ('Address {}'.format(id(L))) #ADDRESS OF THE CHANGED INT IS SAME AS BEFORE
#Hence this synthex is immutable because of tuple and str