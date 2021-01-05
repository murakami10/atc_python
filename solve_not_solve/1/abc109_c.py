
def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


N, X = map(int, input().split())

ls = list(map(lambda x: abs(int(x) - X), input().split()))

ans = ls[-1]
for i in range(len(ls) - 1):
    ans = gcd(ans, ls[i])

print(ans)

# https://atcoder.jp/contests/abc109/tasks/abc109_c
