
def dfs(y: int, x: int):
    island[y][x] = 0
    for dy, dx in dxdy:
        if y+dy >= 0 and y+dy < h and x+dx >= 0 and x+dx < w and island[y+dy][x+dx] == 1:
            dfs(y+dy, x+dx)

    return

w, h = map(int, input().split())

island = [list(map(int, input().split())) for i in range(h)]

dxdy = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]

count = 0


for i in range(h):
    for j in range(w):
        if island[i][j] == 1:
            dfs(i, j)
            count += 1

print(count)

#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp