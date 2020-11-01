
def dfs_countable(x: int, pre: int) -> bool:
    check_num[x] = 1
    for i in range(N):
        if i == pre:
            continue

        if vertex[x][i] == 1:
            if check_num[i] == 1:
                return False
            if not dfs_countable(i, x):
                return False

    return True


N, M = map(int, input().split())

vertex = [[0]*N for i in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    vertex[x-1][y-1] = 1
    vertex[y-1][x-1] = 1

check_num = [0]*N

count = 0

for i in range(N):
    if check_num[i] == 0:
        if dfs_countable(i, i):
            count+=1

print(count)

#https://atcoder.jp/contests/arc037/tasks/arc037_b