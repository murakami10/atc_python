from typing import List, Tuple

N, C = map(int, input().split())

events: List[Tuple[int, int]] = []

for _ in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    events.append((a, c))
    events.append((b, -c))


events.sort(key=lambda x: x[0])


top: int = 0
ans: int = 0
tmp: int = 0
for event in events:
    if event[0] != top:
        ans += min(C, tmp) * (event[0] - top)
        top = event[0]
    tmp += event[1]


print(ans)
# https://atcoder.jp/contests/abc188/tasks/abc188_d
