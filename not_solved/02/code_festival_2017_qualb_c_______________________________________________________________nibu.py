import sys  # 再帰の制限
sys.setrecursionlimit(10**8)


def dfs(x: int, p: int, c: int)-> bool:
    global color

    for i in relation[x]:
        if i == p:
            continue

        if color[i] != -1:
            if color[i] == c:
                return False

        else:
            color[i] = c ^ 1
            if not dfs(i, x, c ^ 1):
                return False

    return True


N, M = map(int, input().split())

relation = [[] for _ in range(N+1)]
color = [-1] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

color[1] = 0
if not dfs(1, 0, 0):
    ans = N*(N-1)//2 - M
    print(ans)
    exit()

c_num = 0
for i in color:
    if i == 0:
        c_num += 1

print(c_num*(N-c_num) - M)

# https://atcoder.jp/contests/code-festival-2017-qualb/tasks/code_festival_2017_qualb_c

