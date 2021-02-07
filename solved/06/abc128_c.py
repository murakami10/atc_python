from typing import List

N, M = map(int, input().split())

S: List[List[int]] = []
for _ in range(M):
    s = [int(x) for i, x in enumerate(input().split()) if i != 0]
    S.append(s)
p = [int(x) for x in input().split()]

count: int = 0
for i in range(2 ** (N)):
    st: set = set()
    for j in range(N):
        if i & (1 << j):
            st.add(j + 1)

    count_flag: bool = True
    for j in range(len(S)):
        tmp: int = 0
        for k in S[j]:
            if k in st:
                tmp ^= 1
        if p[j] != tmp:
            count_flag = False
            break
    if count_flag:
        count += 1
print(count)
# https://atcoder.jp/contests/abc128/tasks/abc128_c
