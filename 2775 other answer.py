repeat = int(input())
for i in range(repeat):
    people = []
    k = int(input())
    n = int(input())
    for floor in range(k + 1):
        people.append([])
        for house in range(1, n + 1):
            if not floor:
                people[-1].append(house)
            else:
                people[floor].append(sum(people[floor - 1][:house]))
    print(people[-1][-1])