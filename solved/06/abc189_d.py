N = int(input())

S = []
for i in range(N):
    S.append(str(input()))


ans = [[0] * (N + 1) for _ in range(2)]
ans[0][0] = 1
ans[1][0] = 1

for i in range(len(S)):
    if S[i] == "AND":
        ans[0][i + 1] = ans[0][i]
        ans[1][i + 1] = 2 * ans[1][i] + ans[0][i]
    else:
        ans[0][i + 1] = 2 * ans[0][i] + ans[1][i]
        ans[1][i + 1] = ans[1][i]


print(ans[0][-1])
# https://atcoder.jp/contests/abc189/tasks/abc189_d
