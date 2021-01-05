from typing import Tuple
import sys
sys.setrecursionlimit(10**8)


def gcd(m: int, n: int) -> int:
    while n:
        m, n = (n, m % n)
    return m


def extra_gcd(m: int, n: int) -> Tuple[int, int, int]:
    if n:
        d, b, a = extra_gcd(n, m % n)
        b = b - (m//n)*a
        return d, a, b

    return m, 1, 0


def lcm(m: int, n: int) -> int:
    return m // gcd(m, n) * n
