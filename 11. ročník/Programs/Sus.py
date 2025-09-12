lines = [list(map(int, line.split())) for line in open("../tohle_zmen.txt").read().splitlines()[1:]]
output = open("../Solution.txt", "w")

for line in lines:
    print(2*line[0]-line[-1], file=output)
