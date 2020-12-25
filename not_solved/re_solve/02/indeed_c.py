
N, M = map(int, input().split())

dp = [[[0]*102 for _ in range(102)] for _ in range(102)]

for _ in range(N):
    a, b, c, w = map(int, input().split())
    dp[a][b][c] = max(dp[a][b][c], w)

for a in range(101):
    for b in range(101):
        for c in range(101):
            dp[a+1][b][c] = max(dp[a][b][c], dp[a+1][b][c])
            dp[a][b+1][c] = max(dp[a][b][c], dp[a][b+1][c])
            dp[a][b][c+1] = max(dp[a][b][c], dp[a][b][c+1])

for _ in range(M):
    x, y, z = map(int, input().split())
    print(dp[x][y][z])
