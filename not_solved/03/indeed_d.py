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


H, W = map(int, input().split())
Sx, Sy = map(int, input().split())
Gx, Gy = map(int, input().split())

p = []

for _ in range(H):
    p.append(list(map(int, input().split())))


hp = []

for i in range(W):
    for j in range(H):
        if i != W-1:
            heapq.heappush(hp, [-p[j][i] * p[j][i+1], i+(j*W), i+1+(j*W)])
        if j != H-1:
            heapq.heappush(hp, [-p[j][i] * p[j+1][i], i+(j*W), i+(j*W)+W])

uf = UnionFind(W*H-1)

ans = 0

while hp:
    item = heapq.heappop(hp)
    if uf.same_check(item[1], item[2]):
        continue
    uf.unit(item[1], item[2])
    ans += -item[0]

for i in range(H):
    ans += sum(p[i])

print(ans)

# https://atcoder.jp/contests/indeednow-finalb-open/tasks/indeednow_2015_finalb_d