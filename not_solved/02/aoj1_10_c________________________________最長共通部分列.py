
N = int(input())

for _ in range(N):
    X = input()
    Y = input()

    dp = [[0]*(len(X) + 1) for _ in range(len(Y) + 1)]

    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i] == Y[j]:
                dp[j+1][i+1] = dp[j][i] + 1
            else:
                dp[j+1][i+1] = max(dp[j+1][i], dp[j][i+1])

    print(dp[len(Y)][len(X)])

#https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_10_C