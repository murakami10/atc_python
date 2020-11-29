import sys
sys.setrecursionlimit(1000000)


def dfs(y, x):
    global maze
    if maze[y][x] == 'g':
        return True
    maze[y][x] = '#'
    answer = False
    for direct in dy_dx:
        dy, dx = direct
        if H > y+dy >= 0 and W > x+dx >= 0 and maze[y+dy][x+dx] in ['.', 'g']:
            answer = dfs(y + dy, x + dx)

        if answer:
            return answer

    return False


H, W = map(int, input().split())

maze = [list(input()) for _ in range(H)]

dy_dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(H):
    for j in range(W):
        if maze[i][j] == 's':
            ans = dfs(i, j)

if ans:
    print('Yes')
else:
    print('No')

#https://atcoder.jp/contests/atc001/tasks/dfs_a