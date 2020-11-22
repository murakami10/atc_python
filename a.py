import bisect

N = int(input())

circle = [list(map(int, input().split())) for _ in range(N)]

left_right = []
for i in range(N):
    left_right.append([circle[i][0] - circle[i][1], circle[i][0] + circle[i][1]])

left_right.sort(key=lambda lr: -lr[1])
left_right.sort(key=lambda lr: -lr[0])

dp = [float('inf')] * N

for i in range(N):
    dp[bisect.bisect_left(dp, left_right[i][1])] = left_right[i][1]

print(bisect.bisect_left(dp, float('inf')))


