from typing import List

N, K = map(int, input().split())
A: List[int] = list(map(lambda x: int(x) - 1, input().split()))

tele: List[List[int]] = [[0] * len(A) for _ in range(61)]

for i in range(len(A)):
    tele[0][i] = A[i]

for i in range(60):
    for j in range(len(A)):
        tele[i + 1][j] = tele[i][tele[i][j]]

curr: int = 0
for i in range(60):
    if K & (1 << i):
        curr = tele[i][curr]

print(curr + 1)

# https://atcoder.jp/contests/abc167/tasks/abc167_d

# 参考にした記事
# https://drken1215.hatenablog.com/entry/2020/06/20/190700
