import time

s = time.time()
for _ in range(5):
    print(_)
    for _ in range(20, 30):
        print(_)
e = time.time()
print(e-s)