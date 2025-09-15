def get_x_y(n):
    b,l = 0, lambda r: (2+3*r)*(r+1)//2 
    while l(2**b) < n: b+=1
    r = int(2**(b-1))
    for i in range(b, -1, -1):
        if l(r+2**i) < n: r+=2**i
    r,i = r+1, 1+3*(r+1)-n+l(r) if r % 2 else n-l(r)-1
    return (-r, i) if i <= r else ((-2*r+i, r) if i <= 2*r else (i-2*r, 3*r-i))

def triangle(a,b,c):
    A,B,C = sorted([get_x_y(o) for o in [a,b,c]])
    d = C[0]-A[0]
    t = B[0] == C[0] and d == C[1]-B[1]
    if A[1] != C[1] or not ((t or (A[0] == B[0] and d == B[1]-A[1]))): return -1
    if d % 3 != 0: return 0
    x,y = (C[0]-d//3, C[1]-d//3) if t else (A[0]+d//3, A[1]+d//3)
    r,i = ((-x, y) if -x >= y else (y, 2*y + x)) if x <= 0 else (x + y, 3*x + 2*y)
    return (2+3*(r-1))*(r)//2 + (1+3*r-i if r%2==0 else i +1)

for _ in range(int(input())): print(triangle(*map(int, input().split(" "))))
    