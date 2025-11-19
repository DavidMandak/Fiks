import heapq
import time


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
        else:
            result = djikstra_solve(n, node_paths, sets)
        print("\n".join(result), file=output)


def tree_solve(n: int, node_paths: list, sets: list) -> list:
    root = 0
    parent = [None]*n
    parent[root] = -1
    stack = [root]
    pre_order = []
    while stack:
        v = stack.pop()
        pre_order.append(v)
        for u, w in node_paths[v]:
            if parent[u] is None:
                parent[u] = v
                stack.append(u)

    for S in sets:
        k = len(S)

        subtree_count = [0]*n
        for s in S:
            subtree_count[s] = 1

        subtree_reachability = [0]*n
        for i in range(len(pre_order)-1, -1, -1):
            v = pre_order[i]
            for u, w in node_paths[v]:
                if parent[u] == v:
                    subtree_count[v] += subtree_count[u]
                    subtree_reachability[v] += subtree_reachability[u]+subtree_count[u]*w

        reachability = [0]*n
        reachability[root] = subtree_reachability[root]
        for v in pre_order:
            for u, w in node_paths[v]:
                if parent[u] == v:
                    # reachability[v] = reachability[u]-subtree_count[v]*w+(k-subtree_count[v])*w
                    reachability[u] = reachability[v]+w*(k-2*subtree_count[u])

        yield str(min(reachability))


def djikstra_solve(n: int, node_paths: list, sets: list) -> list:
    for S in sets:
        reachability = [0]*n

        for s in S:
            heap = [(0, s)]
            dist = [float("inf")]*n
            dist[s] = 0

            while heap:
                d, v = heapq.heappop(heap)

                if d == dist[v]:
                    for u, w in node_paths[v]:
                        check_d = d+w
                        if check_d < dist[u]:
                            dist[u] = check_d
                            heapq.heappush(heap, (check_d, u))

            for i in range(n):
                reachability[i] += dist[i]

        yield str(min(reachability))


s = time.time()
if __name__ == "__main__":
    main()
print(time.time()-s)

import Check
