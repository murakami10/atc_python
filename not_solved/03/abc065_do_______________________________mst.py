import heapq
import itertools


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

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


N = int(input())

point = []
hp = []

for i in range(N):
    x, y = map(int, input().split())
    point.append([x, y, i])

point.sort(key=lambda x: x[0])

for i in range(N - 1):
    maximum = abs(point[i][0] - point[i + 1][0])
    heapq.heappush(hp, (maximum, point[i][2], point[i + 1][2]))

point.sort(key=lambda x: x[1])
for i in range(N - 1):
    maximum = abs(point[i][1] - point[i + 1][1])
    heapq.heappush(hp, (maximum, point[i][2], point[i + 1][2]))


uf = UnionFind(N)
ans = 0
while hp:
    item = heapq.heappop(hp)
    if uf.same_check(item[1], item[2]):
        continue
    uf.unit(item[1], item[2])
    ans += item[0]

print(ans)

# https://atcoder.jp/contests/abc065/tasks/arc076_b
