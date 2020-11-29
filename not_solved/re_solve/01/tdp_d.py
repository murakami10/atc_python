
N, D = map(int, input().split())

num2 = 0
num3 = 0
num5 = 0

while D % 2 == 0:
    num2 += 1
    D /= 2

while D % 3 == 0:
    num3 += 1
    D /= 3

while D % 5 == 0:
    num5 += 1
    D /= 5

# if num2 == 0 and num3 == 0 and num5 == 0 and D != 1: # これはだめ
if D != 1:  # これはいい
    print('0')
    exit()

dp = [[[[0]*(num5+1) for _ in range(num3+1)] for _ in range(num2+1)] for _ in range(N+1)]

c2 = [0, 1, 0, 2, 0, 1]
c3 = [0, 0, 1, 0, 0, 1]
c5 = [0, 0, 0, 0, 1, 0]

dp[0][0][0][0] = 1

for i in range(N):
    for k2 in range(num2+1):
        for k3 in range(num3+1):
            for k5 in range(num5+1):
                for dice in range(6):
                    next5 = min(k5 + c5[dice], num5)
                    next3 = min(k3 + c3[dice], num3)
                    next2 = min(k2 + c2[dice], num2)
                    dp[i+1][next2][next3][next5] += dp[i][k2][k3][k5]/6

print(dp[N][num2][num3][num5])

# https://atcoder.jp/contests/tdpc/tasks/tdpc_dice