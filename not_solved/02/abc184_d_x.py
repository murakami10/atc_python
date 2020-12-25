
A, B, C = map(int, input().split())

dp = [[[0]*101 for _ in range(101)] for _ in range(101)]

dp[A][B][C] = 1
ans = 0

for i in range(A, 101):
    for j in range(B, 101):
        for k in range(C, 101):
            if i == 100 or j == 100 or k == 100:
                ans += dp[i][j][k] *((i+j+k)-(A+B+C))
                continue

            dp[i+1][j][k] += dp[i][j][k] * (i/(i+j+k))
            dp[i][j+1][k] += dp[i][j][k] * (j/(i+j+k))
            dp[i][j][k+1] += dp[i][j][k] * (k/(i+j+k))

print("{:.9f}".format(ans))

# https://www.youtube.com/watch?v=aprT0NP8pOQ&ab_channel=%E3%81%8B%E3%81%A4%E3%81%A3%E3%81%B1%E7%AB%B6%E3%83%97%E3%83%AD 参考
# https://atcoder.jp/contests/abc184/tasks/abc184_d