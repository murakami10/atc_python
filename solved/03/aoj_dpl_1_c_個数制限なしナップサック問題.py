
N, W = map(int, input().split())

dp = [[0]*(W+1) for _ in range(N+1)]

ws = []
vs = []

for _ in range(N):
    v, w = map(int, input().split())
    vs.append(v)
    ws.append(w)


for i in range(N):
    for j in range(W+1):
        if j >= ws[i]:
            dp[i+1][j] = max(dp[i+1][j-ws[i]]+vs[i] ''', dp[i][j-ws[i]]+vs[i]''' , dp[i][j]) # dp[i][j-ws[i]]+vs[i]はなくていい dp[i+1][j-ws[i]]+vs[i]がすでに含んでいるから
        else:
            dp[i+1][j] = dp[i][j]

print(dp[-1][-1])

#https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_C