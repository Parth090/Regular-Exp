import re

f = open('sample.txt','r')

pattern = r'\d{3} \d{3}-\d{4}'
for i in f.readlines():
    search2 = re.findall(i)
    print(search2)
    

f.close()