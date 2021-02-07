import collections

from typing import Dict

N = int(input())

ans: int = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        continue
    tmp_i: int = i
    table: Dict[int, int] = collections.defaultdict(lambda: 0)
    for j in range(2, int(pow(i, 0.5)) + 1):
        while tmp_i % j == 0:
            tmp_i //= j
            table[j] += 1
    if tmp_i != 1:
        table[tmp_i] += 1

    count: int = 1
    for key, value in table.items():
        count *= value + 1

    if count == 8:
        ans += 1

print(ans)
# https://atcoder.jp/contests/abc106/tasks/abc106_b
