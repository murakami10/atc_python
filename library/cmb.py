from typing import List, Tuple


def cmb(n: int, k: int, mod: int, fact: List[int], inv_fact: List[int]) -> int:
    k = min(k, n - k)
    return (fact[n] * inv_fact[k] * inv_fact[n - k]) % mod


def make_table(mod: int, n: int) -> Tuple[List[int], List[int]]:

    fac: List[int] = [1, 1]
    ifac: List[int] = [1, 1]
    inverse: List[int] = [0, 1]
    for i in range(2, n + 1):
        fac.append(fac[i - 1] * i % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        ifac.append(ifac[i - 1] * inverse[i] % mod)
    return ifac, inverse
