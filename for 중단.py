# #원하는 것 : c가 나오면 멈추고 싶음
# #예상 : 1 a , 1 b, 1 c

# for i in (1,2,3):
#     for j in ('a','b','c'):
#         print(i,j)
#         if j=='c':
#             break
# #출력 : 전부 다 나옴


outdoor=True

for i in (1,2,3):
    if not outdoor : break
    else: 
        for j in ('a','b','c'):
            print(i,j)
            if j=='c':
                outdoor=False
                break
