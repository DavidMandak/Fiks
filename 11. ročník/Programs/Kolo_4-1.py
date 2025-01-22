import math

lines = open("../Inputs/test.txt").read().splitlines()
output = open("../Solution", "w")



def diagonals(k, pos, layer, start, end):
    corner_a = end-layer
    corner_b = start+layer
    if pos >= corner_a:
        a = k*layer
    else:
        a = k*(layer-(corner_a-pos))
    if pos <= corner_b:
        b = -k*layer
    else:
        b = -k*(layer-(pos-corner_b))
    return a, b


for problem in lines[1:]:
    tiles = {}
    for pos in list(map(int, problem.split())):
        layer = int((1+math.sqrt(1+24*(pos-1)))//6)
        end = (layer+1)*(3*(layer+1)-1)//2
        start = layer*(3*layer-1)//2+1
        if layer % 2:
            negative, positive = diagonals(1, pos, layer, start, end)
        else:
            positive, negative = diagonals(-1, pos, layer, start, end)
        tiles[pos] = [positive, negative]
    
    exit(tiles)
