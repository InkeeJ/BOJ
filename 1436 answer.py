import re
devil = re.compile('[6]{3}')
i = 0
n = int(input())
j=666
while i<n:
    if not devil.search(str(j)):
        j +=1
        
    else:
        j+=1
        i+=1
        print(i,':',j-1, end='] [')