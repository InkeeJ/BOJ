
def distance_square(point1=tuple,point2=tuple):
    return (point1[0]-point2[0])**2+(point1[1]-point2[1])**2

for i in range(int(input())):
    x=0
    points=list(map(int,input().split()))
    start=(points[0],points[1])
    end=(points[2],points[3])
    stellars = []
    for i in range(int(input())):
        stellars.append(tuple(map(int,input().split())))    
    for b in stellars:
        center =(b[0],b[1])
        r = b[2]**2
        d1 = distance_square(start, center)
        d2 = distance_square(end, center)
        if (d1-r)*(d2-r) <= 0:
            x += 1  
    print(x)


