import heapq


def dai(start: int, edge: list) -> list:
    ans = [float('inf')] * n
    ans[start] = 0
    hp = [(0, start)]
    while hp:
        item = heapq.heappop(hp)
        fm = item[1]
        point_cost = item[0]
        if ans[fm] != point_cost:
            continue
        for to, to_cost in edge[fm]:
            if ans[to] > to_cost + point_cost:
                ans[to] = to_cost + point_cost
                heapq.heappush(hp, (ans[to], to))
    return ans


n, m, s, t = map(int, input().split())

edge_money = [[] for _ in range(n)]
edge_snu = [[] for _ in range(n)]

for _ in range(m):
    u, v, a, b = map(int, input().split())
    u -= 1
    v -= 1
    edge_money[u].append((v, a))
    edge_snu[u].append((v, b))

    edge_money[v].append((u, a))
    edge_snu[v].append((u, b))

ans_money = dai(s-1, edge_money)
ans_snu = dai(t-1, edge_snu)


ans = []
for index, money_snu in enumerate(zip(ans_money, ans_snu)):
    heapq.heappush(ans, [money_snu[0] + money_snu[1], index+1])


tmp_ans = [0, 0]
for i in range(n):
    while True:
        if tmp_ans[1] > i:
            break
        tmp_ans = heapq.heappop(ans)
    print(10**15 - tmp_ans[0])

# https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_d