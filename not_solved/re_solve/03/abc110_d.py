from collections import defaultdict
from typing import Dict
from typing import List
from typing import Tuple


def cmb(n: int, k: int, mod: int, fact: List[int], inv_fact: List[int]) -> int:
    return (fact[n] * inv_fact[k] * inv_fact[n - k]) % mod


def make_table(mod: int, n: int) -> Tuple[List[int], List[int]]:

    fac: List[int] = [1, 1]
    ifac: List[int] = [1, 1]
    inverse: List[int] = [0, 1]
    for i in range(2, n + 1):
        fac.append(fac[i - 1] * i % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        ifac.append(ifac[i - 1] * inverse[i] % mod)
    return fac, ifac


N, M = map(int, input().split())
tmp_M = M
so_insuu: Dict[int, int] = defaultdict(int)
for i in range(2, int(pow(M, 0.5)) + 1):
    while tmp_M % i == 0:
        so_insuu[i] += 1
        tmp_M = tmp_M // i
if tmp_M != 1:
    so_insuu[tmp_M] += 1

mx = 1
for item in so_insuu.values():
    mx = max(mx, item)

mod: int = 10 ** 9 + 7
fa, ifa = make_table(mod, mx + N - 1)

ans = 1
for value in so_insuu.values():
    ans *= cmb(value + N - 1, N - 1, mod, fa, ifa)
    ans %= mod

print(ans)
