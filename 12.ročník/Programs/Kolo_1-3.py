problems = open("../test.txt").read().splitlines()
output = open("../Solution.txt", "w")
line = 1

for i in range(int(problems[0])):
    width, height = (map(int, problems[line].split()))
    x_finish, y_finish = (map(int, problems[line+1].split()))
    line += 2
    grid = []
    for y in range(height):
        grid.append(width*["."])
    explosion = [h.split() for h in problems[line:line+5]]
    line += 5
    for x, y in [(map(int, obstacle.split())) for obstacle in problems[line+1:line+int(problems[line])+1]]:
        grid[y][x] = "0"
    line += int(problems[line])+1
    print(grid)
