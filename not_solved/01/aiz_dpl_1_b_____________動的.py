

N, W = map(int, input().split())

vs = []
ws = []

for _ in range(N):
    v, w = map(int, input().split())
    vs.append(v)
    ws.append(w)

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if j < ws[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j - ws[i]]+vs[i])


print(dp[N][W])

#https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_B