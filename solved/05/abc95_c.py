A, B, C, x, y = map(int, input().split())

larger: int = max(x, y)

com: int = 2 * C if A + B > 2 * C else A + B

ans: int = 0
if x == larger:
    ans = y * com
    tmp = min(A, C * 2)
    ans += (x - y) * tmp
else:
    ans = x * com
    tmp = min(B, C * 2)
    ans += (y - x) * tmp

print(ans)
# https://atcoder.jp/contests/abc095/tasks/arc096_a
