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
    h = None
    corners = []
    for line in range(1, 4):
        for i in range(3):
            control = tiles[i][line]
            for tile in tiles[:i]+tiles[i+1:]:
                if control == tile[line]:
                    check[i] += 1
                    if line == 3:
                        corners.append(tile[1]+tile[2])
                        h = tile[3]
    if  len(corners) == 2 and all(n == 2 for n in check):
        dist = abs(corners[0]-corners[1])//2
        if not dist % 3:
            width = (corners[0]+corners[1])//2
            height = h+(dist//3)
            if height >= abs(width)+2:
                lay = height
                if lay % 2:
                    k = 1
                else:
                    k = -1
                print(lay*(3*lay-1)//2+1+lay+(lay+k*width)//2, file=output)
            else:
                lay = (abs(width)+height)//2
                if (width < 0 and lay % 2) or (width > 0 and not lay % 2):
                    print(lay*(3*lay-1)//2+1+height, file=output)
                else:
                    print((lay+1)*(3*(lay+1)-1)//2-height, file=output)
        else:
            print(0, file=output)
    else:
        print(-1, file=output)
