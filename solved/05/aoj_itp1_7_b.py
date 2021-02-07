while True:
    n, x = map(int, input().split())
    if (n, x) == (0, 0):
        break
    count: int = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if n + 1 > x - i - j > j:
                count += 1
    print(count)

# https://onlinejudge.u-aizu.ac.jp/problems/ITP1_7_B
