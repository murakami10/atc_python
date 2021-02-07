n = int(input())
A = list(map(int, input().split()))
q = int(input())
ms = list(map(int, input().split()))

st: set = set()
for i in range(1 << n + 1):
    tmp: int = 0
    for j in range(n):
        if i & (1 << j):
            tmp += A[j]
    st.add(tmp)


for m in ms:
    if m in st:
        print("yes")
    else:
        print("no")
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_5_A
