a = [0, 1, 2, 3, 4, 5]
b = a
a[2] += 1
print(a)
print(b)
import sys
from collections import deque

def solve():
    sys.setrecursionlimit(1 << 25)
    input_data = open("../input (1).txt").read().strip().split()
    it = iter(input_data)
    t = int(next(it))
    results = []
    for _ in range(t):
        w, h = int(next(it)), int(next(it))
        tx, ty = int(next(it)), int(next(it))

        # načtení tvaru exploze
        offsets = []
        for i in range(5):
            for j in range(5):
                c = next(it)
                if c == "x":
                    offsets.append((j - 2, i - 2))  # dx, dy

        o = int(next(it))
        blocked_input = [(int(next(it)), int(next(it))) for _ in range(o)]

        M = 2
        W, H = w + 2 * M, h + 2 * M

        def inside(x, y):
            return 0 <= x < W and 0 <= y < H

        def to_ext(x, y):
            return x + M, y + M

        tx, ty = to_ext(tx, ty)

        blocked = [[0] * W for _ in range(H)]
        blocked_list = []
        for bx, by in blocked_input:
            ex, ey = to_ext(bx, by)
            if (ex, ey) != (tx, ty):
                blocked[ey][ex] = 1
                blocked_list.append((ex, ey))

        # startovní pozice = prstenec 1 okolo mapy
        starts = []
        ox0, ox1 = M - 1, M + w
        oy0, oy1 = M - 1, M + h
        for x in range(ox0, ox1 + 1):
            if 0 <= x < W:
                if 0 <= oy0 < H:
                    starts.append((x, oy0))
                if 0 <= oy1 < H:
                    starts.append((x, oy1))
        for y in range(oy0, oy1 + 1):
            if 0 <= y < H:
                if 0 <= ox0 < W:
                    starts.append((ox0, y))
                if 0 <= ox1 < W:
                    starts.append((ox1, y))
        starts = list(set(starts))

        blasts = 0
        solved = False

        while True:
            # BFS přes volná políčka
            vis = [[0] * W for _ in range(H)]
            dq = deque()
            for sx, sy in starts:
                if inside(sx, sy) and not blocked[sy][sx] and not vis[sy][sx]:
                    vis[sy][sx] = 1
                    dq.append((sx, sy))
            while dq:
                cx, cy = dq.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = cx + dx, cy + dy
                    if inside(nx, ny) and not vis[ny][nx] and not blocked[ny][nx]:
                        vis[ny][nx] = 1
                        dq.append((nx, ny))

            if vis[ty][tx]:
                print(str(blasts))
                solved = True
                break

            # pokusíme se odblokovat nová políčka
            still_blocked = []
            to_clear = []
            for bx, by in blocked_list:
                can = False
                for ox, oy in offsets:
                    cx, cy = bx - ox, by - oy
                    if inside(cx, cy) and vis[cy][cx]:
                        can = True
                        break
                if can:
                    to_clear.append((bx, by))
                else:
                    still_blocked.append((bx, by))
            if not to_clear:
                print("ajajaj")
                break
            for bx, by in to_clear:
                blocked[by][bx] = 0
            blocked_list = still_blocked
            blasts += 1

    print("\n".join(results))


if __name__ == "__main__":
    solve()
