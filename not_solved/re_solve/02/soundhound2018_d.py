from typing import List
import heapq

def dfs(start: int, edge: List[List[int]]):
    cost = [float('inf')] * (n+1)
    cost[start] = 0
    heap = [(0, start)]

    while heap:
        top = heapq.heappop(heap)
        if cost[top[1]] != top[0]:
            continue

        for i in edge[top[1]]:
            if cost[i[1]] > cost[top[1]] + i[0]:
                cost[i[1]] = cost[top[1]] + i[0]
                heapq.heappush(heap, (cost[i[1]], i[1]))

    return cost


n, m, s, t = map(int, input().split())

edge_money = [[] for _ in range(n+1)]
edge_snu = [[] for _ in range(n+1)]

for _ in range(m):
    v, u, a, b = map(int, input().split())
    edge_money[v].append((a, u))
    edge_money[u].append((a, v))

    edge_snu[v].append((b, u))
    edge_snu[u].append((b, v))

cost_money = dfs(s, edge_money)
cost_snu = dfs(t, edge_snu)

heap = []

for i in range(n+1):
    heapq.heappush(heap, (cost_snu[i] + cost_money[i], i))

ans = heapq.heappop(heap)
for i in range(n):
    while True:
        if ans[1] > i:
            break
        ans = heapq.heappop(heap)
    print(10**15 - ans[0])



# https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_d