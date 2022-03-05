construction_time=[0, 10, 20, 1, 5, 8, 7, 1, 43]
dic={2:[1], 3:[1], 4:[2], 5:[2], 6:[3], 7:[5,6], 8:[7]}
x=dic[7]
time = construction_time[7]
def isit(x):
    if x in dic:
        return dic[x][0]