Given_number = int(input("Enter a number: ")) #To find the user input
if Given_number > 1: #should be greater than 1
    for i in range(2, Given_number):
        if (Given_number % i) == 0: #by moduler function i defined
            print(Given_number, "is not a prime number")
            break #Used break to stop the loop
    else:
        print(Given_number, "is a prime number")
else: #to close the 1st loop if value is >=1
    print(Given_number, "is not a prime number")