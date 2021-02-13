import sys
from typing import Tuple

sys.setrecursionlimit(10 ** 8)


# 拡張ユークリッド法
def extra_gcd(m: int, n: int) -> Tuple[int, int, int]:
    if n:
        d, b, a = extra_gcd(n, m % n)
        b = b - (m // n) * a
        return d, a, b

    return m, 1, 0


def mod_inv(a: int, mod: int) -> int:
    """
    逆元を求める
    :param a: 逆元を求める数
    :param mod: mod
    :return: 逆元
    """
    d, x, y = extra_gcd(a, mod)
    if d != 1:
        print("modular inverse does not exist")
        exit()
    else:
        return x % mod
