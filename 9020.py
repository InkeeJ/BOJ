import sys


def isprime(m):
    for i in range(2,int(m**(1/2))+1):
        if m%i ==0 : return False
    return True
for _ in range(int(sys.stdin.readline().rstrip())):
    n=int(sys.stdin.readline().rstrip())
    (p,q)=(n/2,n/2)
    while not all([isprime(p), isprime(q)]): p=p-1; q=q+1
    print(int(p),int(q))

#input 쓸때보다 2배 빠름