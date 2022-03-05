# from collections import deque
# number = deque()
# for i in range(1,10001):
#     number.append(i)
# def d(n:int) -> int :
#     m=str(n)
#     l=0
#     for k in m:
#         l+=int(k)
#     return n+l
# i=0
# try:
#     while number[i]:
#         try:
#             n=number[i]
#             while d(n)<=10000:
#                 number.remove(d(n))
#                 n=d(n)
#         except ValueError:
#             pass
#         i += 1
# except IndexError:
#     pass
# for i in number:
#     print(i)


isSelfNum = [True] * 10001


def d(n):
    nextNum = n + sum(map(int, list(str(n))))
    if nextNum > 10000:
        return
    isSelfNum[nextNum] = False
    d(nextNum)



for i in range(1, 10000):
    if isSelfNum[i]:
        print(i)
        d(i)


# y = set(range(1, 10001))
# n = set()

# for i in range(1, 10001):      
#     for j in str(i):  
#         i += int(j)
#     n.add(i) 

# self_num = sorted(y - n)
# for i in self_num:
#     print(i)