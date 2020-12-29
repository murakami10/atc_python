import bisect

N = int(input())

circles = []

for _ in range(N):
    x, r = map(int, input().split())
    circles.append((x+r, x-r))

circles.sort(key=lambda x: -x[1])
circles.sort(key=lambda x: -x[0])


dp = [float('inf')] * N

for circle in circles:
    left = bisect.bisect_left(dp, circle[1])
    dp[left] = circle[1]

print(bisect.bisect_left(dp, float('inf')))



# https://atcoder.jp/contests/tdpc/tasks/tdpc_target
