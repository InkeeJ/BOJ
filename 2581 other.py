def isPrime(a):
    if a == 1: return False
    for i in range(2,a):
        if a%i == 0: return False
    return True
l = list(filter(isPrime, list(range(int(input()),int(input())+1))))
if not l:
    print(-1)
else:
    print(sum(l))
    print(l[0])