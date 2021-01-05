import itertools

N, M, R = map(int, input().split())

rs = list(map(int, input().split()))

dp = [[float('inf')]*N for _ in range(N)]

for i in range(N):
    dp[i][i] = 0


for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dp[a][b], dp[b][a] = (c, c)


for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

ans = float('inf')

for i in itertools.permutations(rs, len(rs)):
    pre = i[0]
    tmp = 0
    for j in range(1, len(i)):
        tmp += dp[pre-1][i[j]-1]
        pre = i[j]
    ans = min(ans, tmp)

print(ans)

# https://atcoder.jp/contests/abc073/tasks/abc073_d
