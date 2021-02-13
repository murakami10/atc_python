import sys

sys.setrecursionlimit(10 ** 8)


def gcd(m: int, n: int) -> int:
    """
    最大公約数をもとめる
    :param m: 数
    :param n: 数
    :return: 最大公約数
    """
    while n:
        m, n = (n, m % n)
    return m


def lcm(m: int, n: int) -> int:
    """
    mとnの最小公倍数を求める
    :param m: 数字
    :param n: 数字
    :return: 最小公約数
    """
    return m // gcd(m, n) * n
