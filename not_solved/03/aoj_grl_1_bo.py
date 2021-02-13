v, e, r = map(int, input().split())

edges = []

for _ in range(e):
    s, t, w = map(int, input().split())
    edges.append((s, t, w))

num = 0
cost = [float("inf")] * v
cost[r] = 0

while True:
    flag = True

    for edge in edges:
        s, t, w = edge
        if cost[t] > cost[s] + w:
            cost[t] = cost[s] + w
            flag = False

    if flag:
        break

    if num == v:
        print("NEGATIVE CYCLE")
        exit()
    num += 1

for i in cost:
    if i == float("inf"):
        print("INF")
    else:
        print(i)

# https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B
