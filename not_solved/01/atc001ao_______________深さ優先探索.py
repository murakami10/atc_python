import sys
sys.setrecursionlimit(1000000)

def dfs(y: int, x: int) -> int:
    ans = 0
    field[y][x] = '#'
    for dx, dy in dxdy:
        if x+dx >= 0 and x+dx < W and y+dy >= 0 and y+dy < H:
            if field[y+dy][x+dx] == 'g':
                return 1
            if field[y+dy][x+dx] == '.':
                ans = dfs(y+dy,x+dx)
        
        if ans == 1:
            return ans
    
    return ans

H,W = map(int, input().split())

field = [list(input()) for i in range(H)]

dxdy = [[1,0],[0,-1],[-1,0],[0,1]]

ans = 0

for i in range(H):
    for j in range(W):
        if field[i][j] == 's':
            ans = dfs(i, j)

if ans:
    print('Yes')
else:
    print('No')

#defaultだと再帰の回数に引っかかるので
#import sys
#sys.setrecursionlimit(1000000)
#解けてないわけじゃないが時間がかかった

#https://atcoder.jp/contests/atc001/tasks/dfs_a