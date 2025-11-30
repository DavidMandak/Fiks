lines = open("test.txt").read().splitlines()
output = open("12.ročník/Solution.txt", "w")

t = int(lines[0])
i = 1
for _ in range(t):
    n, m = map(int, lines[i])
    parent = [None]*n
    kids = {}
    i += 1

    for __ in range(m):
        line = lines[i].split()
        l = line[0]
        kids[l] = []
        for li in line[2:]:
            kids[l].append(li)
            parent[li] = l
        i += 1
    
    a, b = map(int, lines[i])
    parent_find = [None]*a
    kids_find = {}
    i += 1

    for __ in range(m):
        line = lines[i].split()
        l = line[0]
        kids_find[l] = []
        for li in line[2:]:
            kids_find[l].append(li)
            parent_find[li] = l
        i += 1

    pass
