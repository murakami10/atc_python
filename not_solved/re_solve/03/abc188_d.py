from typing import List
from typing import Tuple

N, C = map(int, input().split())

paths: List[Tuple[int, int]] = []

for _ in range(N):
    a, b, c = map(int, input().split())
    paths.append((a, c))
    paths.append((b + 1, -c))

paths.sort(key=lambda x: x[0])
tmp_money = 0
ans = 0
pre = 0
for path in paths:

    if pre == path[0]:
        tmp_money += path[1]
        continue

    ans += (path[0] - pre) * min(tmp_money, C)
    tmp_money += path[1]
    pre = path[0]

print(ans)
