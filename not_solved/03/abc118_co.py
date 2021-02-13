def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


N = int(input())

x = list(map(int, input().split()))


ans = x[-1]
for i in range(len(x) - 1):
    ans = gcd(ans, x[i])

print(ans)

# https://atcoder.jp/contests/abc118/tasks/abc118_c
