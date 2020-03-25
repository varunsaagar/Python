first_name='varun'
last_name='saagar'

#In 3.6 below syntax can be used
fullname=f'{first_name} {last_name}'
message = f'Hello , {fullname.title()}!' #title is a method that makes the formating all first words to upper cares
print(f'Hello , {fullname.title()}')

#But in 3.5 older versions

fullname='{}'.format(first_name,last_name).title() # What will happen if we use single bracs to store two parentheses.
print(fullname)

#f-string is for format , python formats the string by replacing the name of any variable in braces its value