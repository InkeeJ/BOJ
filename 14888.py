import math


def f(num1,num2,x):
    if x == '+' : return num1+num2
    elif x == '-' : return num1-num2
    elif x == '*' : return num1 * num2
    elif x == '/' :
        if num1 <0 : return -(math.floor(-num1/num2))
        else: return num1//num2
    else: return

dict={0:'+',1:'-',2:'*',3:'/'}

n=int(input())
nums=list(map(int,input().split()))
operations=list(map(int,input().split()))
words=[]
memory=[]
def making_words(k): #k : operation index
    global memory, word
    if k == n-1:
        words.append(word)
        return
    else:
        for j in range(4):
            if operations[j]==0:
                continue
            else:
                if not memory : word = dict[j] 
                else:word = memory[-1]+dict[j]
                if word in memory :
                    continue 
                else:
                    memory.append(word)
                    operations[j] -=1
                    making_words(k+1)
                    operations[j] +=1
                    memory.pop()
making_words(0)

max=-10**9
min=10**9
def go():
    global max, min
    for operation in words:
        ind=0
        num=nums[ind]
        for j in operation:
            ind+=1
            num=f(num,nums[ind],j)
        if max<num : max=num
        if min>num : min=num
go()
print(max)
print(min)