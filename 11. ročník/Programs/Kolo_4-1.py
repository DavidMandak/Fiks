import math

lines = open("../Inputs/test.txt").read().splitlines()
output = open("../Solution.txt", "w")


def diagonals(k, pos, layer, start, end):
    corner_a = end-layer
    corner_b = start+layer
    c = None
    if pos >= corner_a:
        a = k*layer
        c = end-pos
    else:
        a = k*(layer-(corner_a-pos))
        c = layer
    if pos <= corner_b:
        b = -k*layer
        c = pos-start
    else:
        b = -k*(layer-(pos-corner_b))
        if not c:
            c = layer
    return a, b, c


for problem in lines[1:]:
    tiles = []
    for pos in list(map(int, problem.split())):
        layer = int((1+math.sqrt(1+24*(pos-1)))//6)
        end = (layer+1)*(3*(layer+1)-1)//2
        start = layer*(3*layer-1)//2+1
        if layer % 2:
            negative, positive, row = diagonals(1, pos, layer, start, end)
        else:
            positive, negative, row = diagonals(-1, pos, layer, start, end)
        tiles.append([pos, positive, negative, row])
    check = [0]*3
    for line in range(1, 4):
        for i in range(3):
            for tile in tiles[:i]+tiles[i+1:]:
                pass
    exit()
