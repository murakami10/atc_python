N, M = map(int, input().split())

A = []

for i in range(N):
    A.append(list(map(int, input().split())))

ans: int = 0

for i in range(M):
    for j in range(i + 1, M):
        tmp_count: int = 0
        for k in range(N):
            tmp_count += max(A[k][i], A[k][j])

        ans = max(ans, tmp_count)

print(ans)
# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c
