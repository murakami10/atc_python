import copy
import itertools

def deep_explore(x: int, ls: list):
    global count
    for i in range(N):
        if i not in ls and rela[x][i] == 1:
            ls_copy =ls.copy()
            ls_copy.append(i)
            deep_explore(i, ls_copy)

    if len(ls) == N:
        count += 1

N, M = map(int, input().split())

rela = [[0] * N for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    rela[a-1][b-1] = 1
    rela[b-1][a-1] = 1

count = 0
ls = [0]
#deep_explore(0, ls)
start = 0
for i in itertools.permutations(range(N), N):
    if start == i[0]:
        count_flag = True
        for j in range(N):
            if j==1:
                continue
            if not rela[i[j-1]][i[j]]:
                count_flag = False
        if count_flag:
            count += 1

print(count)

#グローバル変数
#permutations
#https://atcoder.jp/contests/abc054/tasks/abc054_c