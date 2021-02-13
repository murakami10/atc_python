import collections

N = int(input())

table = collections.defaultdict(int)

for i in range(2, N + 1):
    tmp = i
    for j in range(2, int(pow(i, 0.5)) + 1):
        while tmp % j == 0:
            tmp //= j
            table[j] += 1

    if tmp != 1:
        table[tmp] += 1

ans = 1

for key, item in table.items():
    ans *= (item + 1) % (pow(10, 9) + 7)
    ans %= pow(10, 9) + 7

print(ans)

# https://atcoder.jp/contests/abc052/tasks/arc067_a
