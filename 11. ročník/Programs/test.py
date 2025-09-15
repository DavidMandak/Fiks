mine = open("../Solution.txt").read().splitlines()
sol = open("../Solution1.txt").read().splitlines()
file = open("../input.txt").read().splitlines()
for i in range(len(mine)):
    if mine[i] != sol[i]:
        print(file[i+1], "\n", mine[i], "\n", sol[i])