def isPrime(a):
    if a == 1: return False
    for i in range(2,a):
        if a%i == 0: return False
    return True
input()
a = len(list(filter(isPrime,list(map(int, input().split())))))
print(a)