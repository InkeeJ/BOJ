dic = {1:1, 2:1}

def f(n):
    if n == 0:
        return 0
    if n in dic:
        return dic[n] 
    else:
        dic[n] = f(n-1)+f(n-2)
        return dic[n]
for i in range(int(input())):
    n=int(input())
    if n == 0:
        print(1,0)
    else:
        print(f(n-1), f(n))