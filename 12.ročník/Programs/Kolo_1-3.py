from collections import deque

problems = open("../test.txt").read().splitlines()
output = open("../Solution.txt", "w")
line = 1

for i in range(int(problems[0])):
    width, height = (map(int, problems[line].split()))
    x_finish, y_finish = (map(int, problems[line+1].split()))

    line += 2
    edge = 1
    width += 2*edge
    height += 2*edge
    grid = []
    for y in range(height):
        grid.append(width*[0])
    explosion_map = [h.split() for h in problems[line:line+5]]
    explosion = []
    for y in range(5):
        for x in range(5):
            if explosion_map[y][x] == "x" and (y, x) != (2, 2):
                explosion.append((x-2, y-2))

    line += 5
    for x, y in [(map(int, obstacle.split())) for obstacle in problems[line+1:line+int(problems[line])+1]]:
        grid[y+1][x+1] = 2
    line += int(problems[line])+1
    for y in grid:
        print(y)
    print()

    starts = deque()
    for y in range(1, height-1):
        starts.append((0, y))
        starts.append((width-1, y))
    for x in range(2, width-2):
        starts.append((x, 0))
        starts.append((x, height-1))

    count = 0
    while True:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        while starts:
            sx, sy = starts.popleft()
            grid[sy][sx] = 1
            for dx, dy in directions:
                if not grid[sy+dy][sx+dx]:
                    starts.append((sx+dx, sy+dy))

        if grid[y_finish][x_finish]:
            print(count, file=output)


