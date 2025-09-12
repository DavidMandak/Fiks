lines = open("../test.txt").read().splitlines()

pos = 1
for _ in range(int(lines[0])):
    r, s = map(int, lines[pos].split())
    sectors = list(map(int, lines[pos+1]))
    robots =
