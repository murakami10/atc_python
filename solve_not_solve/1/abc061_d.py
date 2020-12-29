
N, M = map(int, input().split())

edges = []

for _ in range(M):
    s, t, w = map(int, input().split())
    edges.append((s, t, w))

cost = [-float('inf')] * (N+1)
cost[1] = 0

num = 0

while True:

    flag = True
    pre_n = cost[N]

    for edge in edges:
        s, t, w = edge
        if cost[t] < cost[s] + w:
            cost[t] = cost[s] + w
            flag = False

    if flag:
        break

    if num == M+1:
        if pre_n == cost[N]:
            break
        print('inf')
        exit()
    num += 1

print(cost[N])
# https://atcoder.jp/contests/abc061/tasks/abc061_d
