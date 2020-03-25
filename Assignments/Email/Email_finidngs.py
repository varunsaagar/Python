import re

email1=open('emaildata.txt',)
lines=email1.readlines()

for line in lines:
    print(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', line))

# patterns = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# matches = patterns.finditer(email)
#
# for data in matches:
#     print(data)

