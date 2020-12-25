

class UnionFind:

    def __init__(self, n: int):
        self.parent = [i for i in range(n+1)]
        self.rank   = [0]*(n+1)

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unit(self, x: int, y: int):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        else:
            self.parent[parent_y] = parent_x
            if self.rank[parent_y] == self.rank[parent_x]:
                self.rank[parent_x] += 1

    def same_check(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


N, Q = map(int, input().split())

uf1 = UnionFind(N*2)

for _ in range(Q):
    w, x, y, z = map(int, input().split())
    if w == 1:
        if z%2 == 0:
            uf1.unit(x, y)
            uf1.unit(x + N, y + N)
        else:
            uf1.unit(x, y+N)
            uf1.unit(x+N, y)


    else:
        if uf1.same_check(x, y):
            print('YES')
        else:
            print('NO')