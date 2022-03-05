v = set()
for i in range(10**4):
    t = str(i).zfill(4)
    v |= {int(f'{t[:j]}666{t[j:4]}') for j in range(5)}
print(sorted(v)[int(input())-1])