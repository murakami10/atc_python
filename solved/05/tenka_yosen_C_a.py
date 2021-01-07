from typing import List

n = int(input())
if n == 1:
    print(0)
    exit()

"""

count: int = 0

for i in range(2, n):
    for j in range(2, int(pow(i, 0.5)) + 1):
        if i % j == 0:
            break
    else:
        count += 1

print(count)
"""

table: List[int] = [0] * n
table[0] = -1
table[1] = -1

for i in range(2, int(pow(n, 0.5)) + 1):
    if table[i] == -1:
        continue
    for j in range(2, n + 1):
        if i * j >= n:
            break
        table[i * j] = -1

count = 0
for i in table:
    if i == -1:
        continue
    count += 1

print(count)

# https://atcoder.jp/contests/tenka1-2012-qualc/tasks/tenka1_2012_9
