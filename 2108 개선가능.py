n=int(input())
import sys
y=[0]*(8001)
x=[]
for i in range(n):
    j=int(sys.stdin.readline().rstrip())
    x.append(j)
    y[j+4000]+=1
print(round(sum(x)/n))
x.sort()
print(x[int((n-1)/2)])
m=max(y)
if y.count(m) > 1 :
    y[y.index(m)]-=1
    print(y.index(m)-4000)
else:
    print(y.index(m)-4000)
print(max(x)-min(x))

#개선 힌트 : y만 가지고 해보시길