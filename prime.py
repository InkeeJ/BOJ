def isprime(m):
    for i in range(2,int(m**(1/2))+1):
        if m%i ==0 : return False
    return True

print(isprime(4))