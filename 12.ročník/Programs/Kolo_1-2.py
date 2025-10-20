def setup(stations: list) -> list:
    loops = []
    for i in range(len(stations)):
        if not stations[i]:
            continue
        j = stations[i] - 1
        loops.append(1)
        while j != i:
            k = j
            j = stations[j] - 1
            loops[-1] += 1
            stations[k] = 0
    return loops


def divide(loops: list, start: int, end: int) -> None:
    if start < end:
        middle = (start+end)//2
        divide(loops, start, middle)
        divide(loops, middle+1, end)
        merge(loops, start, end, middle)


def merge(loops: list, start: int, end: int, middle: int) -> None:
    left_list = loops[start:middle+1]
    right_list = loops[middle+1:end+1]

    l = 0
    r = 0
    i = start
    while l < len(left_list) and r < len(right_list):
        left_num = left_list[l]
        right_num = right_list[r]
        if left_num >= right_num:
            loops[i] = left_num
            l += 1
        else:
            loops[i] = right_num
            r += 1
        i += 1

    while l < len(left_list):
        loops[i] = left_list[l]
        l += 1
        i += 1
    while r < len(right_list):
        loops[i] = right_list[r]
        r += 1
        i += 1


def type_0(loops: list, goal: int) -> int:
    total = 0
    length = loops[0]
    i = 1
    while length < goal:
        length += loops[i]
        i += 1
        total += 1
    return total


def type_1_high(loops: list, goal: int) -> int:
    total = 0
    i = 0
    while i < len(loops) and loops[i] > goal:
        total += -(-loops[i] // goal) - 1
        i += 1
    return total


def type_1_low(loops: list, goal: int) -> int:
    length = 0
    i = -1
    while length < goal:
        i += 1
        length += loops[i]
    if length == goal:
        return i
    if i == subset_find(loops, goal)-1:
        return i
    return i+1


def subset_find(loops: list, goal: int) -> int:
    last = [-1]*(goal+1)
    current = [-1]*(goal+1)
    last[0] = 0

    for amount in range(1, len(loops)+ 1):
        for num in range(goal+1):
            check = num-loops[amount-1]
            if check < 0:
                current[num] = last[num]
            else:
                if last[check] != -1 and (last[num] == -1 or last[check]+1 < last[num]):
                        current[num] = last[check]+1
                else:
                    current[num] = last[num]
        last = current.copy()
    return last[goal]


def solve(loops: list, goal: int, t: int) -> int:
    match t:
        case 0:
            return type_0(loops, goal)
        case 1:
            if loops[0] >= goal:
                return type_1_high(loops, goal)
            else:
                return type_1_low(loops, goal)
    return None


if __name__ == "__main__":
    lines = open("input.txt").read().splitlines()
    output = open("Solution.txt", "w")
    for line in range(1, 2*int(lines[0])+1, 2):
        amount, goal, t = map(int, lines[line].split())
        stations = list(map(int, lines[line+1].split()))

        if goal > amount:
            print("ajajaj", file=output)
            continue

        loops = setup(stations)

        divide(loops, 0, len(loops)-1)

        answer = solve(loops, goal, t)
        print(answer, file=output)
