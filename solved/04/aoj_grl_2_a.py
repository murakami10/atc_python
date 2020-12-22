import heapq


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


v, e = map(int, input().split())

edge = []

for _ in range(e):
    s, t, w = map(int, input().split())
    heapq.heappush(edge, (w, s, t))

uf = UnionFind(v)
ans = 0
while edge:
    item = heapq.heappop(edge)
    if uf.same_check(item[1], item[2]):
        continue
    uf.unit(item[1], item[2])
    ans += item[0]

print(ans)

# https://onlinejudge.u-aizu.ac.jp/problems/GRL_2_A

