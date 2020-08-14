class Employee:

    raise_amount=1.10

    def __init__(self , first , last , pay):
        self.first=first
        self.last=last
        self.pay= pay
        self.email=first + '.' + last +"@ashok.com"

    def  fullname(self):
        return '{}{}'.format(self.first,self.last)

    def x_raise(self):
        self.pay = int(self.pay *self.raise_amount)

    @classmethod
    def set_raiseamt(cls , amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str1.split('-')
        return cls(first, last, pay)

emp1 = Employee('varun', 'saagar',60000)
emp2 = Employee('prasanth' , ' venkat' , 60000)
emp3 = Employee('ruthra','pathy' , 60000)

Employee.set_raiseamt(1.05)

Employee.raise_amount = 1.10

print(Employee.raise_amount)

print(emp1.raise_amount)

print(emp2.raise_amount)
# emp1.x_raise()
# print(emp1.pay)
# # print(emp1.pay)
# emp2.raise_amount=1.15
#
# emp2.x_raise()
#
# print(emp2.pay)
#
# emp3.x_raise()
# print(emp3.pay)
#
# print(Employee.x_raise)

emp_str1= 'Varun-Saagar-70000'
emp_str2='Prasanth-Venakt-30000'
emp_str3='Rthra-Pathy-400000'

first,last,pay = emp_str1.split('-')

newemp1 = Employee(first,last,pay)
#
# print(newemp1.email)
# print(newemp1.pay)



# emp1.fullname()
# print(Employee.fullname(emp1))
# print(emp1)
# print(emp1)

# print(emp1.email )
# print(emp2.email )
# print('{}{}'.format(emp1.first,emp1.last))