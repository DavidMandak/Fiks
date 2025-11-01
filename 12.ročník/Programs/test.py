a = open("../Solution.txt").read()
b = open("../check.txt", "w")
print(a, file=b)