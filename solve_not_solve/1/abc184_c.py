
# A: x1+y1 = x2+y2
# B: x1-y1 = x2-y2
# C: |x1-x2| + |y1-y2| <= 3

# 0手 一致
# 1手 A, B, Cのどれかで行ければいい
# 2手 AB AC BC CC
def solve(r1, c1, r2, c2):

    if r1 == r2 and c1 == c2:
        return 0

    if r1+c1 == r2+c2:
        return 1

    if r1-c1 == r2-c2:
        return 1

    if abs(r1-r2) + abs(c1-c2) <= 3:
        return 1

    if (r1+c1)%2 == (r2+c2)%2:
        return 2

    if abs((r1+c1) - (r2+c2)) <= 3:
        return 2

    if abs((r1-c1) - (r2-c2)) <= 3:
        return 2

    if abs(r1 - r2) + abs(c1 - c2) <= 6:
        return 2

    return 3


r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

print(solve(r1, c1, r2, c2))

