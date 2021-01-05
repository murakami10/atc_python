from typing import Tuple


def extra_gcd(m: int, n: int) -> Tuple[int, int, int]:
    if n:
        d, b, a = extra_gcd(n, m % n)
        b = b - (m//n)*a
        return d, a, b

    return m, 1, 0


a, b = map(int, input().split())

d, x, y = extra_gcd(a, b)

print(x, y)

# https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_E
