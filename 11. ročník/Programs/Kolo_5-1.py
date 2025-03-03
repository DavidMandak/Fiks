from collections import defaultdict
import time

lines = open("../Inputs/input (1).txt").read().splitlines()
output = open("../Solution.txt", "w")

start = time.time()
n = 1
for _ in range(int(lines[0])):
    s = int(lines[n])+1
    if not 5 <= _ <= 8:
        total = 0
        strings = defaultdict(list)
        for seq in lines[n+1:n+s]:
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
    n += s
print((time.time()-start))


