from typing import Tuple
import sys
sys.setrecursionlimit(10**8)


def extra_gcd(m: int, n: int) -> Tuple[int, int, int]:
    if n:
        d, b, a = extra_gcd(n, m % n)
        b = b - (m//n)*a
        return d, a, b

    return m, 1, 0


def mod_inv(a: int, b: int) -> int:
    d, x, y = extra_gcd(a, b)
    if d != 1:
        print("modular inverse does not exist")
        exit()
    else:
        return x % b
