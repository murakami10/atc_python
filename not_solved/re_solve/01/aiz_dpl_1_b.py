

N, W = map(int, input().split())


vw = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(W+1) for _ in range(N+1)]


for i in range(N):
    for j in range(W+1):
        if j >= vw[i][1]:
            dp[i+1][j] = max(dp[i][j], dp[i+1][j-vw[i][1]]+vw[i][0])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[-1][-1])
#https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_C