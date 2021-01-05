
def gcd(x: int, y: int) -> int:
    if y == 0: return x
    return gcd(y, x % y)

N = int(input())

if N == 1:
    x = int(input())
    print(x)
    exit()

t = []

for _ in range(N):
    x = int(input())
    t.append(x)

tmp = gcd(t[0], t[1])
tmp = t[0] * t[1] // tmp
ans = tmp
for i in range(2, len(t)):
    ans = gcd(t[i], tmp)
    tmp = t[i]*tmp // ans
    ans = tmp

print(ans)
# https://atcoder.jp/contests/abc070/tasks/abc070_c
