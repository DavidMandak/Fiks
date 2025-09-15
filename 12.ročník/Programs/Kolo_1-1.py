lines = [list(map(int, line.split())) for line in open("../input.txt").read().splitlines()[1:]]
output = open("../Solution.txt", "w")


def gcd(a, b):
    if b > a:
        temp = a
        a = b
        b = temp
    while a % b:
        temp = b
        b = a % b
        a = temp
    return b

for a, b, c in lines:
    if not a < c > b and not c % gcd(a, b):
        print("pujde to", file=output)
    else:
        print("ajajaj", file=output)
