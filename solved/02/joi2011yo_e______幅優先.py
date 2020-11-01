import collections

def bfs(y: int, x: int, gy: int, gx: int) -> int:
    queue = collections.deque()
    point = [[float("inf")]* W for _ in range(H)]

    queue.append([y,x])
    point[y][x] = 0
    while queue:
        q = queue.popleft()
        for dy, dx in dxdy:
            if q[0]+dy >= 0 and q[0]+dy < H and q[1]+dx >= 0 and q[1]+dx < W and point[q[0]+dy][q[1]+dx] == float("inf") and m[q[0]+dy][q[1]+dx] != 'X':
                point[q[0]+dy][q[1]+dx] = point[q[0]][q[1]] + 1
                queue.append([q[0]+dy, q[1]+dx])
        if q[0] == gy and q[1] == gx:
            return point[q[0]][q[1]]




H, W, N = map(int, input().split())

m = [list(input()) for i in range(H)]

dxdy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

start = [[0,0]]*(N+1)
end   = [[0,0]]*N

for i in range(H):
    for j in range(W):
        if m[i][j] == 'S':
            start[0] = [i, j]
        elif m[i][j].isdecimal():
            start[int(m[i][j])] = [i, j]
            end[int(m[i][j])-1] = [i, j]

cost = 0
for i in range(N):
    cost += bfs(start[i][0], start[i][1], end[i][0], end[i][1])

print(cost)

#https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e
#str.isdecimal()
#collections.deque()
#float("inf")