import heapq
from typing import List


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


H, W = map(int, input().split())

sx, sy = map(int, input().split())

gx, gy = map(int, input().split())

P = []

ans = 0

for _ in range(H):
    ps = list(map(int, input().split()))
    ans += sum(ps)
    P.append(ps)

heap = []

for h in range(H):
    for w in range(W):
        if w != W - 1:
            heapq.heappush(heap, (-P[h][w] * P[h][w + 1], (W * h) + w, (W * h) + w + 1))

        if h != H - 1:
            heapq.heappush(
                heap, (-P[h][w] * P[h + 1][w], (W * h) + w, (W * (h + 1)) + w)
            )

uf = UnionFind(H * W)
while heap:
    pop = heapq.heappop(heap)
    if uf.same_check(pop[1], pop[2]):
        continue

    ans += -pop[0]
    uf.unit(pop[1], pop[2])
print(ans)
