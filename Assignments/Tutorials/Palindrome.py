a=input('Type the word you wanna check:')
b=a[ : :-1] #Using slicing methodolgy
if a!=b:
    print('Nope,its not a palindrome')
else:
    print('Yup,its palindrome')

