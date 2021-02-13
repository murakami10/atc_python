def kouyaku(a: int, b: int) -> int:

    if b == 0:
        return a
    else:
        return kouyaku(b, a % b)


N = int(input())

ts = []
for _ in range(N):
    ts.append(int(input()))

ans = 1
for t in ts:
    ans = ans * t // kouyaku(ans, t)

print(ans)
