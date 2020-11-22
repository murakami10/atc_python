
n, m, l, x = map(int, input().split())
a = list(map(int, input().split()))

dp = [[10 ** 10] * m for i in range(n + 1)]

# dp[i + 1][j] := i 番目のタンクまでで番号 j の休憩所にいるための最小周回数
dp[0][0] = 1
for i in range(n):
    for j in range(m):
        dp[i + 1][(j + a[i]) % m] = min(dp[i][(j + a[i]) % m], dp[i][j] + (j + a[i]) // m)

if dp[n][l] <= x:
    print("Yes")
else:
    print("No")

# https://atcoder.jp/contests/maximum-cup-2018/tasks/maximum_cup_2018_d

'''
N, M, L, X = map(int, input().split())
energy = list(map(int, input().split()))

tmp_step = [0] * M
next_step = [0] * M

tmp_step[0] = 1

for i in range(N):
    for j in range(M):
        rest = j - energy[i]
        count = 0
        while rest < 0:
            rest += M
            count += 1
        if tmp_step[rest] > 0:
            if tmp_step[j] == 0:
                next_step[j] = tmp_step[rest]+count
            else:
                next_step[j] = min(tmp_step[rest]+count, tmp_step[j])
        else:
            next_step[j] = tmp_step[j]

    tmp_step = next_step.copy()
    next_step = [0] * M


if X >= tmp_step[L] > 0:
    print('Yes')
else:
    print('No')
'''