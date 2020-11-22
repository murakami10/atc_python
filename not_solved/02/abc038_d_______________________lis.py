import bisect

N = int(input())

boxs = [list(map(int, input().split())) for _ in range(N)]

boxs.sort(key=lambda box: -box[0])
boxs.sort(key=lambda box: box[1])

dp = [float('inf')] * N

for i in range(N):
    dp[bisect.bisect_left(dp, boxs[i][0])] = boxs[i][0]

print(bisect.bisect_left(dp, float('inf')))

# https://atcoder.jp/contests/abc038/tasks/abc038_d