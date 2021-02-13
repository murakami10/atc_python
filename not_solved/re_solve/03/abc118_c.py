from typing import List


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


N = int(input())

A: List[int] = list(map(int, input().split()))
ans = A[0]
for a in A:
    ans = gcd(a, ans)
print(ans)
