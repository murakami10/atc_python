import heapq

v, e, start = map(int, input().split())

edge = [[] for _ in range(v)]

for _ in range(e):
    s, t, d = map(int, input().split())
    edge[s].append((t, d))

vertex = [float('inf')] * v
ans = [float('inf')] * v

vertex[start] = 0
ans[start] = 0
heap = [[0, start]]

while heap:
    top = heapq.heappop(heap)
    if ans[top[1]] != top[0]:
        continue

    for to in edge[top[1]]:
        if ans[to[0]] > top[0] + to[1]:
            ans[to[0]] = top[0] + to[1]
            heapq.heappush(heap, [ans[to[0]], to[0]])

for i in ans:
    if i == float('inf'):
        print('INF')
    else:
        print(i)

# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_A


