class employee:
     salary_increment=1.05

     no_employee=0

     def __init__(self,first,last,pay):
         self.first=first
         self.last=last
         self.pay=pay
         employee.no_employee +=1

     def email(self):
         self.email= self.first + '.' + self.last + '@ashokleyland.com'

     def fullname(self):
        return '{}{}'.format(self.first,self.last)

     def get_increment(self):
        self.pay= int(self.pay * self.salary_increment)

emp_1=employee('varun','saagar',20000)
emp_2=employee('prasanth' , 'venkat' , 18000)
emp_3=employee('naveen','prasath',19500)
employee.no_employee
emp_1.email()
emp_2.email()
emp_3.email()
emp_1.fullname()
emp_2.fullname()
emp_3.fullname()
emp_1.get_increment()
emp_2.get_increment()
emp_3.get_increment()

print(emp_1.pay,emp_1.email,emp_1.fullname)
print(emp_2.pay,emp_2.email,emp_2.fullname)
print(emp_3.pay,emp_3.email,emp_3.fullname())

