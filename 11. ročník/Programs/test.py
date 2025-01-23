from collections import defaultdict

a = defaultdict(int)

b = [0, 1, 2, 0, 2, 5]
for c in b:
    a[c] += 1
print(a)
