import heapq
from typing import List
from typing import Tuple


class UnionFind:
    def __init__(self, number: int):
        self.parent: List[int] = [i for i in range(number + 1)]
        self.order: List[int] = [0] * (number + 1)

    def find(self, index: int) -> int:

        parent: int = self.parent[index]

        if parent == index:
            return index
        else:
            parent = self.find(parent)
            self.parent[index] = parent
            return parent

    def same_check(self, first_item: int, second_item: int) -> bool:
        return self.find(first_item) == self.find(second_item)

    def unit(self, first_item: int, second_item: int):

        first_item_parent = self.find(first_item)
        second_item_parent = self.find(second_item)

        if self.order[first_item_parent] > self.order[second_item_parent]:
            self.parent[second_item_parent] = first_item_parent
        else:
            self.parent[first_item_parent] = second_item_parent
            if self.order[first_item_parent] == self.order[second_item_parent]:
                self.order[second_item_parent] += 1


N = int(input())

xs = []
ys = []
for i in range(N):
    x, y = map(int, input().split())
    xs.append((x, i))
    ys.append((y, i))

xs.sort()
ys.sort()

heap: List[Tuple[int, int, int]] = []

for i in range(N - 1):
    heapq.heappush(heap, (xs[i + 1][0] - xs[i][0], xs[i + 1][1], xs[i][1]))
    heapq.heappush(heap, (ys[i + 1][0] - ys[i][0], ys[i + 1][1], ys[i][1]))

uf = UnionFind(N)
ans: int = 0
while heap:
    pop = heapq.heappop(heap)
    if uf.same_check(pop[1], pop[2]):
        continue
    ans += pop[0]
    uf.unit(pop[1], pop[2])

print(ans)
