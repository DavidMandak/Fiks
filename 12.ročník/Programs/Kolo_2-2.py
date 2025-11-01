from collections import deque
import time
from Chat import a


def main() -> None:
    lines = open("../input.txt").read().splitlines()
    output = open("../Solution.txt", "w")
    line = 1

    for _ in range(int(lines[0])):
        if _ == 25:
            break
        n, m = map(int, lines[line].split())
        node_paths = [[] for __ in range(n)]

        line += 1
        for __ in range(m):
            u, v, w = map(int, lines[line].split())
            node_paths[u].append((v, w))
            node_paths[v].append((u, w))
            line += 1

        q = int(lines[line])
        line += 1
        sets = []
        for __ in range(q):
            sets.append(list(map(int, lines[line].split()[1:])))
            line += 1

        if m == n-1:
            result = tree_solve(n, node_paths, sets)
            #chat = a(n, node_paths, sets)
            #print(list(result))
            #print(chat)

        else:
            result = djikstra_solve(n, node_paths, sets)
        print("\n".join(result), file=output)


def tree_solve(n: int, node_paths: list, sets: list) -> list:
    root = 0
    parent = [None]*n
    parent[root] = -1
    bfs = deque([root])
    level_order = []
    while bfs:
        u = bfs.pop()
        level_order.append(u)
        for v, w in node_paths[u]:
            if parent[v] is None:
                parent[v] = u
                bfs.appendleft(v)

    for S in sets:
        k = len(S)

        subtree_count = [0]*n
        for v in S:
            subtree_count[v] = 1

        subtree_reachability = [0]*n
        for i in range(len(level_order)-1, -1, -1):
            u = level_order[i]
            for v, w in node_paths[u]:
                if parent[v] == u:
                    subtree_count[u] += subtree_count[v]
                    subtree_reachability[u] += subtree_reachability[v]+subtree_count[v]*w

        reachability = [0]*n
        reachability[root] = subtree_reachability[root]
        for u in level_order:
            for v, w in node_paths[u]:
                if parent[v] == u:
                    # reachability[v] = reachability[u]-subtree_count[v]*w+(k-subtree_count[v])*w
                    reachability[v] = reachability[u]+w*(k-2*subtree_count[v])

        yield str(min(reachability))


def djikstra_solve(n: int, node_paths: list, sets: list) -> list:
    for S in sets:
        reachability = [0]*n

        for source in S:
            bfs = deque([(source, 0)])
            distances = [None]*n
            distances[source] = 0

            while bfs:
                node, dist = bfs.pop()

                if dist == distances[node]:
                    for v, w in node_paths[node]:
                        curr_d = distances[v]
                        check_d = dist+w
                        if curr_d is None or check_d < curr_d:
                            distances[v] = check_d
                            bfs.appendleft((v, check_d))

            for i in range(n):
                reachability[i] += distances[i]

        yield str(min(reachability))


s = time.time()
if __name__ == "__main__":
    main()
print(time.time()-s)
