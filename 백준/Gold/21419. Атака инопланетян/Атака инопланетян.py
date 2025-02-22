import sys
from dataclasses import dataclass

def read_ints():
    return map(int, sys.stdin.readline().split())

@dataclass
class Triangle:
    x: int
    y: int
    side: int
    
    def in_triangle(self, px: int, py: int) -> bool:
        return px >= self.x and py >= self.y and (py + px) <= (self.x + self.side + self.y)
    
    @staticmethod
    def read():
        x, y, s = read_ints()
        return Triangle(2 * x, 2 * y, 2 * s)

def intersect(a: Triangle, b: Triangle) -> Triangle:
    x = max(a.x, b.x)
    y = max(a.y, b.y)
    
    if not a.in_triangle(x, y) or not b.in_triangle(x, y):
        return Triangle(x, y, 0)
    
    low, high = 0, int(1e9)
    while high - low > 1:
        mid = (low + high) // 2
        if not (a.in_triangle(x + mid, y) and a.in_triangle(x, y + mid) and 
                b.in_triangle(x + mid, y) and b.in_triangle(x, y + mid)):
            high = mid
        else:
            low = mid
    
    return Triangle(x, y, low)

def main():
    n = int(sys.stdin.readline())
    tr = Triangle.read()
    
    for _ in range(n - 1):
        tr = intersect(tr, Triangle.read())
    
    print(f"{(tr.side * tr.side) / 8:.3f}")

if __name__ == "__main__":
    main()
