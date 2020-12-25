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

uf = UnionFind(N*2)


for _ in range(Q):
    w, x, y, z = map(int, input().split())

    if w == 1:
        if z%2 == 0:
            uf.unit(x, y)
            uf.unit(x+N, y+N)
        else:
            uf.unit(x, y+N)
            uf.unit(x+N, y)

    else:
        print('YES' if uf.same_check(x, y) else 'NO')


# https://atcoder.jp/contests/arc036/tasks/arc036_d
