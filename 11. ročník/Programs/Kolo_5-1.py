from collections import defaultdict
import time

lines = open("../Inputs/input (1).txt").read().splitlines()
output = open("../Solution.txt", "w")

start = time.time()
pos = 1
for _ in range(int(lines[0])):
    amount = int(lines[pos])
    if not 5 <= _ <= 8:
        total = 0
        strings = defaultdict(list)
        for seq in lines[pos+1:pos+amount+1]:
            strings[len(seq)].append(seq)
        strings = sorted(strings.items())
        length = len(strings)
        for i in range(length):
            for _ in range(len(strings[i][1])):
                sequence = strings[i][1][0]
                strings[i][1].pop(0)
                for j in range(i, length):
                    for seq in strings[j][1]:
                        if sequence in seq:
                            total += 1
        print(total, file=output)
    else:
        print(-1, file=output)
    pos += amount+1
print((time.time()-start))

pos = 1
for _ in range(int(lines[0])):
    amount = int(lines[pos])
    total = 0
    strings = defaultdict(list)
    for seq in lines[pos+1:pos+amount+1]:
        strings[len(seq)].append(seq)
    strings = sorted(strings.items())
    cache = defaultdict(list)
    length = len(strings)
    for l in range(length-1, -1, -1):
        for i in range(len(strings[l][1])):
            sequence = strings[l][1][i]
            for m in range(l, length):
                for j in range(len(strings[m][1])):
                    seq = strings[m][1][j]
                    if (m, j) not in cache[(l, i)] and sequence in seq:
                        total += 1
                        cache[(l, i)].append((m, j))
                        for s in cache[(m, j)]:
                            if s == (l, i):
                                total -= 1
                            elif s not in cache[(l, i)]:
                                total += 1
                                cache[(l, i)].append(s)
    print(total)
    pos += amount+1
