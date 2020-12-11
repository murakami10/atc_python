import collections
import sys
sys.setrecursionlimit(10**8)


def dfs(x: int, c: int):

    global color
    for r in relation[x]:
        if color[r] != -1:
            continue

        if length[(x, r)] % 2 == 0:
            color[r] = c
            dfs(r, c)
        else:
            color[r] = c ^ 1
            dfs(r, c ^ 1)


N = int(input())

color = [-1] * (N+1)
relation = [list() for _ in range(N + 1)]

length = collections.defaultdict(int)

for _ in range(N-1):
    u, v, w = map(int, input().split())
    relation[u].append(v)
    relation[v].append(u)
    length[(u, v)] = w
    length[(v, u)] = w

color[1] = 0
dfs(1, 0)

for i in range(1, N+1):
    print(color[i])


# https://atcoder.jp/contests/abc126/tasks/abc126_d
