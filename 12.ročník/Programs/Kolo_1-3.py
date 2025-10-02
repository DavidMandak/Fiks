from collections import deque

problems = open("../input.txt").read().splitlines()
output = open("../Solution.txt", "w")
line = 1
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


def find():
    global starts
    while starts:
        sx, sy = starts.popleft()
        grid[sy][sx] = 1
        for dx, dy in directions:
            nx, ny = sx+dx, sy+dy
            if 0 <= ny < height and 0 <= nx < width and not grid[ny][nx]:
                starts.append((nx, ny))


def check():
    return grid[y_finish][x_finish]


def unblock():
    global grid, starts
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                grid[y][x] = 3
                for ux, uy in unblock_grid[y][x]:
                    if grid[uy][ux] == 2:
                        grid[uy][ux] = 0
                        starts.append((ux, uy))


def view():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 2:
                print(0, end="")
            elif grid[y][x] == 1:
                print(end="E")
            elif (x, y) == (x_finish, y_finish):
                print(end="X")
            else:
                print(end=" ")
        print()
    print()


for _ in range(int(problems[0])):
    width, height = (map(int, problems[line].split()))
    x_finish, y_finish = (map(int, problems[line+1].split()))

    line += 2
    edge = 1
    width += 2*edge
    height += 2*edge
    x_finish += edge
    y_finish += edge
    grid = []
    unblock_grid = []
    for y in range(height):
        grid.append(width*[0])
        unblock_grid.append([])
        for x in range(width):
            unblock_grid[y].append([])

    explosion_map = [h.split() for h in problems[line:line+5]]
    explosions = []
    for y in range(5):
        for x in range(5):
            if explosion_map[y][x] == "x" and (y, x) != (2, 2):
                explosions.append((x-2, y-2))

    line += 5
    blocked = []
    for x, y in [(map(int, obstacle.split())) for obstacle in problems[line+1:line+int(problems[line])+1]]:
        grid[y+edge][x+edge] = 2
        blocked.append((x+edge, y+edge))
    line += int(problems[line])+1

    starts = deque()
    for y in range(1, height-1):
        starts.append((0, y))
        starts.append((width-1, y))
    for x in range(2, width-2):
        starts.append((x, 0))
        starts.append((x, height-1))

    if not explosions:
        find()
        if check():
            print(0, file=output)
            print(0)
        else:
            print("ajajaj", file=output)
            print("ajajaj")
        continue

    for bx, by in blocked:
        for ex, ey in explosions:
            cx, cy = bx-ex, by-ey
            if 0 <= cx < width and 0 <= cy < height:
                unblock_grid[cy][cx].append((bx, by))

    count = 0
    while True:
        find()

        if check():
            print(count, file=output)
            print(count)
            break

        unblock()

        count += 1
