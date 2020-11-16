
N = int(input())

ls = list(map(int, input().split()))

ans = [[0] * (100*100 + 1) for _ in range(N+1)]

ans[0][0] = 1

for i in range(len(ls)):
    for j in range(100*100):
        if ans[i][j] == 1:
            ans[i+1][j+ls[i]] = 1
            ans[i+1][j] = 1

print(sum(ans[-1]))

#https://atcoder.jp/contests/tdpc/tasks/tdpc_contest