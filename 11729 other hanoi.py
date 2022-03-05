def hanoi(n,start,end,rest):
    if n==1 : print(start,end) #초깃값
    if n>1:
        hanoi(n-1,start,rest,end) #n번째놈의 목적지는 n-1번째의 rest
        print(start,end) #n을 목적지로
        hanoi(n-1,rest,end,start) #rest에 있는 n-1을 end로
n=int(input())
print(2**n-1)
hanoi(n,1,3,2)
        