import queue

R, C = map(int, input().split())
starty, startx = map(int, input().split())
goaly, goalx = map(int, input().split())

maze = [list(input()) for i in range(R)]

q = queue.Queue()

q.put([starty-1,startx-1,0])
dxdy = [[0,1], [0,-1], [1,0], [-1,0]]

maze[starty-1][startx-1] = "#"

while True:
    item = q.get()
    if item[0] == goaly-1 and item[1] == goalx-1:
        print(item[2])
        exit()

    for dx, dy in dxdy:
        if item[0]+dy >= 0 and item[0]+dy < R and item[1]+dx >= 0 and item[1]+dx < C and maze[item[0]+dy][item[1]+dx] == ".":
            maze[item[0]+dy][item[1]+dx] = '#'
            q.put([item[0]+dy, item[1]+dx, item[2]+1])

#https://atcoder.jp/contests/abc007/submissions/me