import bisect

N = int(input())

ans = [-float('inf')]
presents = []
for _ in range(N):
    w, h = map(int, input().split())
    presents.append((w, h))

presents.sort(key=lambda a: -a[1])
presents.sort(key=lambda a: a[0])

for i in presents[::-1]:
    left = bisect.bisect_left(ans, -i[1])
    if left >= len(ans):
        ans.append(-i[1])
    else:
        ans[left] = -i[1]

print(len(ans) - 1)



# https://atcoder.jp/contests/abc038/tasks/abc038_d