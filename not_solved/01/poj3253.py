n = int(input())
L = list(map(int, input().split()))

ans = 0

# 板が1本になるまで適用
while n > 1:
    # 一番短い板 mii1 、次に短い板 mii2 を求める
    mii1 = 0
    mii2 = 1

    if L[mii1] > L[mii2]:
        mii1, mii2 = mii2, mii1

    for i in range(2, n):
        if L[i] < L[mii1]:
            mii2 = mii1
            mii1 = i
        elif L[i] < L[mii2]:
            mii2 = i

    # それらを併合
    t = L[mii1] + L[mii2]
    ans += t

    if mii1 == n - 1:
        mii1, mii2 = mii2, mii1
    L[mii1] = t
    L[mii2] = L[n - 1]
    n -= 1

print(ans)

#http://poj.org/problem?id=3253