from typing import List

n: int = int(input())

A: List[int] = [int(x) for x in input().split()]
st: set = set()
for i in range(2 ** (n + 1)):
    tmp: int = 0
    for j in range(n):
        if i & (1 << j):
            tmp += A[j]
    st.add(tmp)


q = int(input())
ms = [int(x) for x in input().split()]
for m in ms:
    if m in st:
        print("yes")
    else:
        print("no")
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_5_A
