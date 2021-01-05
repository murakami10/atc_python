
N = int(input())

ans = float("inf")

for i in range(1, int(pow(N, 0.5)) + 1):
    if N % i != 0:
        continue
    other = N/i

    count = 0
    while other > 0:
        other //= 10
        count += 1
    ans = min(ans, count)

print(ans)
# https://atcoder.jp/contests/abc057/tasks/abc057_c
