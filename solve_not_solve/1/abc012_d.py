

N, M = map(int, input().split())

edge = [[float('inf')]*N for _ in range(N)]

for _ in range(M):
    a, b, v = map(int, input().split())
    a -= 1
    b -= 1
    edge[a][b], edge[b][a] = (v, v)

for i in range(N):
    edge[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            edge[i][j] = min(edge[i][j], edge[i][k] + edge[k][j])

ans = float('inf')


for i in range(N):
    row_ans = 0
    for j in range(N):
        row_ans = max(row_ans, edge[i][j])
    ans = min(ans, row_ans)

print(ans)

# https://atcoder.jp/contests/abc012/tasks/abc012_4
