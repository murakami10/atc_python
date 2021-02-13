from collections import defaultdict
from typing import Dict

N = int(input())

table: Dict[int, int] = defaultdict(int)

for n in range(2, N + 1):
    tmp_n = n
    for i in range(2, int(pow(n, 0.5)) + 1):

        while tmp_n % i == 0:
            table[i] += 1
            tmp_n //= i

    if tmp_n != 1:
        table[tmp_n] += 1

ans = 1

for key, value in table.items():
    ans *= value + 1
    ans %= 10 ** 9 + 7

print(ans)
