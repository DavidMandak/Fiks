def get_ring_start(n: int) -> int:
    assert n >= 0
    return 1+n*(3*n-1)//2

class DoubledCoord:
    def __init__(self, y: int, x: int) -> None:
        self.y = y
        self.x = x
        assert y % 2 == x % 2

    def __eq__(self, other: 'DoubledCoord') -> bool:
        return (self.y, self.x) == (other.y, other.x)

    def dist(self, other: 'DoubledCoord') -> int:
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        return dy + max(0, (dx - dy) // 2)

    def flip_x(self) -> None:
        self.x *= -1

    def get_ring(self) -> int:
        return self.dist(DoubledCoord(0, 0))
    
    def get_ring_part(self) -> int:
        ring = self.get_ring()
        ring_part = 2
        if ring % 2 == 1:
            if self.y - self.x == 2 * ring and self.y != ring:
                ring_part = 0
            elif self.y == ring and self.x != self.y:
                ring_part = 1
        else:
            if self.y + self.x == 2 * ring and self.y != self.x:
                ring_part = 0
            elif self.y == ring and self.x != -ring:
                ring_part = 1
        return ring_part
    
    @staticmethod
    def get_ring_part_start(n: int, part: int) -> 'DoubledCoord':
        out = DoubledCoord(0, 2 * n)
        if part == 1:
            out = DoubledCoord(n, n)
        elif part == 2:
            out = DoubledCoord(n, -n)
        if n % 2 == 1:
            out.flip_x()
        return out

    def to_seqcoord(self) -> 'SeqCoord':
        if self == DoubledCoord(0, 0):
            return SeqCoord(1)
        ring = self.get_ring()
        ring_part = self.get_ring_part()
        ring_start = get_ring_start(ring)
        out = SeqCoord(ring_start)
        for i in range(ring_part):
            out.x += DoubledCoord.get_ring_part_start(ring, i).dist(DoubledCoord.get_ring_part_start(ring, i + 1))
        out.x += self.dist(DoubledCoord.get_ring_part_start(ring, ring_part))
        return out


class SeqCoord:
    def __init__(self, x: int) -> None:
        assert x >= 1
        self.x = x

    def get_ring(self) -> int:
        if self.x == 1:
            return 0
        l, r = 0, self.x
        while r - l > 1:
            mid = (l+r) // 2
            if self.x >= get_ring_start(mid):
                l = mid
            else:
                r = mid
        return l
    
    def get_ring_part(self) -> int:
        ring = self.get_ring()
        ring_start = get_ring_start(ring)
        if self.x < ring_start + ring:
            return 0
        elif self.x < ring_start + 2 * ring:
            return 1
        return 2
    
    def to_doubledcoord(self) -> DoubledCoord:
        if self.x == 1:
            return DoubledCoord(0, 0)
        ring = self.get_ring()
        ring_part = self.get_ring_part()
        ring_start = get_ring_start(ring)
        out = DoubledCoord(0, 0)
        if ring_part == 0:
            out = DoubledCoord(self.x - ring_start, 2 * ring - (self.x - ring_start))
        elif ring_part == 1:
            out = DoubledCoord(ring, ring - 2 * (self.x - ring_start - ring))
        elif ring_part == 2:
            out = DoubledCoord(ring - (self.x - ring_start - 2 * ring), -ring - (self.x - ring_start - 2 * ring))
        if ring % 2:
            out.flip_x()
        return out

def is_triangle(a: DoubledCoord, b: DoubledCoord, c: DoubledCoord) -> bool:
    print(a.y, b.y, c.y)
    return a.dist(b) == a.dist(c) and a.dist(c) == b.dist(c) and (a.y == b.y or a.y == c.y or b.y == c.y)

def solve() -> None:
    global i
    i += 1
    x, y, z = map(int, lines[i].split())
    assert x != y and y != z and z != x
    a = SeqCoord(x).to_doubledcoord()
    b = SeqCoord(y).to_doubledcoord()
    c = SeqCoord(z).to_doubledcoord()

    if is_triangle(a, b, c) and a.dist(b) % 3 == 0:
        mn = min(a.y, b.y, c.y)
        is_pointing_up = (sum([a.y > mn, b.y > mn, c.y > mn]) == 1)
        
        core = DoubledCoord(
            a.dist(b) // 3 + min(a.y, b.y, c.y) if is_pointing_up else max(a.y, b.y, c.y) - a.dist(b) // 3,
            a.dist(b) + min(a.x, b.x, c.x)
        )
        print(core.to_seqcoord().x, file=output)
        
    elif is_triangle(a, b, c):
        print(0, file=output)
    else:
        print(-1, file=output)

lines = open("test.txt").read().splitlines()
output = open("Solution1.txt", "w")
i = 0
if __name__ == "__main__":
    t = int(lines[0])
    for _ in range(t):
        solve()