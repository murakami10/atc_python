N, X = map(int, input().split())

tmp = 0
for i in range(N):
    v, p = map(int, input().split())
    tmp += v * p
    if tmp > (X * 100):
        print(i + 1)
        exit()
print(-1)

# 不動点小数点の計算は避ける!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# https://atcoder.jp/contests/abc189/tasks/abc189_b
