# #1. for 이용
# n=int(input())
# l=1
# for i in range(n):
#     l=l*(n-i)
# print(l)

#recursively

n=int(input())
def f(n):
    if n==0 : return 1
    return n*f(n-1)
print(f(n))

