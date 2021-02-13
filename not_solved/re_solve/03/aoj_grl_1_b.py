import heapq
from dataclasses import dataclass
from typing import List
from typing import Tuple


@dataclass
class CostVertex:
    count: int
    index: int

    def __lt__(self, other):
        return True


V, E, r = map(int, input().split())

edge: List[List[Tuple[int, int]]] = [[] for _ in range(V)]

for _ in range(E):
    s, t, d = map(int, input().split())
    edge[s].append((d, t))

cost = [float("inf")] * V
cost[r] = 0
heap: List[Tuple[int, CostVertex]] = [(0, CostVertex(0, r))]


while heap:
    top = heapq.heappop(heap)

    if top[1].count > E:
        print("NEGATIVE CYCLE")
        exit()

    for e in edge[top[1].index]:
        (index_cost, index) = e
        if cost[index] <= top[0] + index_cost:
            continue
        cost[index] = top[0] + index_cost
        heapq.heappush(heap, (cost[index], CostVertex(top[1].count + 1, index)))

for c in cost:
    if c == float("inf"):
        print("INF")
    else:
        print(c)
