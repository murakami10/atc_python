from typing import List
from typing import Tuple


def cmb(n: int, k: int, mod: int, fact: List[int], inv_fact: List[int]) -> int:
    """
    nCkを計算する.
    :param n: nCkのn
    :param k: nCkのk
    :param mod: mod
    :param fact: make_talbeのfac
    :param inv_fact: make_tableのifac
    :return: nCkを計算する
    """
    return (fact[n] * inv_fact[k] * inv_fact[n - k]) % mod


def make_table(mod: int, n: int) -> Tuple[List[int], List[int]]:
    """
    nの階乗のテーブルを予め作る.
    :param mod: mod
    :param n: nの階乗まで計算する
    :return: fac[n]がnの階乗, ifac[n]がnの階乗の逆元
    """

    fac: List[int] = [1, 1]
    ifac: List[int] = [1, 1]
    inverse: List[int] = [0, 1]
    for i in range(2, n + 1):
        fac.append(fac[i - 1] * i % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        ifac.append(ifac[i - 1] * inverse[i] % mod)

    return fac, ifac
