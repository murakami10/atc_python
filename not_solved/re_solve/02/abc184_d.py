
A, B, C = map(int, input().split())


dp = [[[0]*102 for _ in range(102)] for _ in range(102)]

dp[A][B][C] = 1

ans = 0

for a in range(A, 101):
    for b in range(B, 101):
        for c in range(C, 101):
            if a == 100 or b == 100 or c == 100:
                ans += (a+b+c - A - B - C)*dp[a][b][c]
            else:
                dp[a][b][c+1] += dp[a][b][c]*(c/(a+b+c))
                dp[a][b+1][c] += dp[a][b][c]*(b/(a+b+c))
                dp[a+1][b][c] += dp[a][b][c]*(a/(a+b+c))
print("{:.9f}".format(ans))

# https://atcoder.jp/contests/abc184/tasks/abc184_d

