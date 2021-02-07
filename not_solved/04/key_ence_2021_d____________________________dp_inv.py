import sys
from typing import Tuple

sys.setrecursionlimit(10 ** 8)


def extra_gcd(m: int, n: int) -> Tuple[int, int, int]:
    if n:
        d, b, a = extra_gcd(n, m % n)
        b = b - (m // n) * a
        return d, a, b

    return m, 1, 0


def mod_inv(a: int, b: int) -> int:
    d, x, y = extra_gcd(a, b)
    if d != 1:
        print("modular inverse does not exist")
        exit()
    else:
        return x % b


H, W, K = map(int, input().split())

table = [["0"] * (W + 1) for _ in range(H + 1)]
dp = [[0] * (W + 1) for _ in range(H + 1)]

for _ in range(K):
    h, w, c = map(str, input().split())
    height: int = int(h) - 1
    width: int = int(w) - 1
    table[height][width] = c

dp[0][0] = 1
# inv = mod_inv(3, 998244353)
# print(inv)
inv = 332748118
for i in range(H):
    for j in range(W):

        dp[i][j] %= 998244353

        if table[i][j] == "0":
            dp[i][j + 1] += dp[i][j] * 2 * inv
            dp[i + 1][j] += dp[i][j] * 2 * inv
        elif table[i][j] == "X":
            dp[i][j + 1] += dp[i][j]
            dp[i + 1][j] += dp[i][j]
        elif table[i][j] == "R":
            dp[i][j + 1] += dp[i][j]
        elif table[i][j] == "D":
            dp[i + 1][j] += dp[i][j]

print(dp[H - 1][W - 1] * pow(3, H * W - K, 998244353) % 998244353)
# https://atcoder.jp/contests/keyence2021/tasks/keyence2021_c
