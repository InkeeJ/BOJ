import re
devil = re.compile('[6]{3}')
devil_4last=re.compile('[6]{4}$')
devil_3last=re.compile('[6]{3}$')
devil_5666=re.compile('[5][6]{3}$')
devil_6670=re.compile('[6][6][7][0]')
# while True:
n=int(input())
i = 1
# end_game = [x for x in range(1,2666800) if '666' in str(x)]

j=666
if n == 1 : print(j)
else:
    while i<n:
        if not devil.search(str(j)) and devil_6670.search(str(j)):
            j=str(j)
            j=j[:-4]+'7666'; j=int(j)
        else:
            if devil_4last.search(str(j)):
                j+=1
                i+=1
            elif devil_5666.search(str(j)):
                j=str(j)
                j=j[:-4]+'6660';j=int(j)
                if '6666' in str(j)[:-1]:
                    j=int(str(j)[:re.compile('[6]{3}[6]+[0]+$').search(str(j)).start()]+'666'+len(str(j)[re.compile('[6]{3}[6]*[0]+$').search(str(j)).start()+3:])*'0')
                i+=1
            elif devil_3last.search(str(j)):
                j+=10**3
                i+=1
            else:
                j+=1
                i+=1
                if devil_6670.search(str(j)) and not devil.search(str(j)):
                    j=str(j)
                    j=j[:-4]+'7666'; j=int(j)
    # if end_game[n-1]!=j : print(n,end_game[n-1],j)    
    # else : print('no pblm')