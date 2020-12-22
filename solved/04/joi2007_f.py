import heapq

def dijkstra(s: int) -> list:
    ans = [float('inf')] * n
    ans[s] = 0
    hp = [(0, s)]
    while hp:
        item = heapq.heappop(hp)
        if item[0] != ans[item[1]]:
            continue

        for to, to_cost in edge[item[1]]:
            if ans[to] > to_cost + item[0]:
                ans[to] = to_cost + item[0]
                heapq.heappush(hp, (ans[to], to))
    return ans


n, k = map(int, input().split())

edge = [[] for _ in range(n)]
for _ in range(k):
    tmp_list = list(map(int, input().split()))
    if tmp_list[0] == 0:
        ans = dijkstra(tmp_list[1]-1)
        to = tmp_list[2]-1
        print(ans[to] if ans[to] != float('inf') else -1)

    else:
        edge[tmp_list[1]-1].append((tmp_list[2]-1, tmp_list[3]))
        edge[tmp_list[2]-1].append((tmp_list[1]-1, tmp_list[3]))

# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f
