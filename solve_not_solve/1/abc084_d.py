from typing import List

Q = int(input())
mx = (10 ** 5) // 2

table: List[int] = [0] * (mx + 1)


for i in range(2, mx + 1):

    for j in range(2, int(pow(i, 0.5)) + 1):
        if i % j == 0:
            table[i] = table[i - 1]
            break
    else:
        other = (i * 2) - 1
        for j in range(2, int(pow(other, 0.5)) + 1):
            if other % j == 0:
                table[i] = table[i - 1]
                break
        else:
            table[i] = table[i - 1] + 1
for i in range(Q):
    left, r = map(int, input().split())
    left = (left + 1) // 2 - 1
    r = (r + 1) // 2
    # print(table[0:10])
    print(table[r] - table[left])
# https://atcoder.jp/contests/abc084/tasks/abc084_d
