N, K = map(int, input().split())

As = list(map(lambda x: int(x) - 1, input().split()))

table = [[0] * N for _ in range(60)]

table[0] = As.copy()

for i in range(59):
    for j in range(N):
        table[i + 1][j] = table[i][table[i][j]]

ans = 0
for i in range(60):
    if K & (1 << i):
        ans = table[i][ans]

print(ans + 1)
