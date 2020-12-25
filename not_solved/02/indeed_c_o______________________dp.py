
N, M = map(int, input().split())

dp = [[[0]*(102) for _ in range(102)] for _ in range(102)]

for _ in range(N):
    a, b, c, w = map(int, input().split())
    dp[a][b][c] = max(dp[a][b][c], w)

for i in range(101):
    for j in range(101):
        for k in range(101):
            curr = dp[i][j][k]
            dp[i][j][k+1] = max(dp[i][j][k+1], curr)
            dp[i+1][j][k] = max(dp[i+1][j][k], curr)
            dp[i][j+1][k] = max(dp[i][j+1][k], curr)

for _ in range(M):
    a, b, c = map(int, input().split())
    print(dp[a][b][c])

    #https://atcoder.jp/contests/indeednow-finala-open/tasks/indeednow_2015_finala_c