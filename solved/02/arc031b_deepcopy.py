import copy
def stuck_island(y: int, x: int) -> int:
    island_stuck = [[y,x]]
    island_copy[y][x] = 'x'

    while island_stuck != []:
        top = island_stuck.pop()
        for dy, dx in dxdy:
            if top[0]+dy >=0 and top[0]+dy < 10 and top[1]+dx >= 0 and top[1]+dx < 10 and island_copy[top[0]+dy][top[1]+dx] == 'o':
                island_stuck.append([top[0]+dy, top[1]+dx])
                island_copy[top[0]+dy][top[1]+dx] = 'x'

    return 0


island = [list(input()) for i in range(10)]

dxdy = [[0,1],[0,-1],[1,0],[-1,0]]

able_islanden = False

for i in range(10):
    for j in range(10):
        if island[i][j] == 'x':
            island_copy = copy.deepcopy(island)
            stuck_island(i, j)
            able_islanden = True
            for i1 in range(10):
                for j1 in range(10):
                    if island_copy[i1][j1] == 'o':
                        able_islanden = False
            if able_islanden:
                break
    if able_islanden:
        break

if not able_islanden:
    print('NO')
    exit()

print('YES')


# island_copy = island.copy()だと浅いコピーになる
# from copy import copy
# x = [[1, 2, 3],4, 5]
# y = copy(x)
# x is y # False
# x[0] is y[0] # True 
#よってdeepcopy

#https://atcoder.jp/contests/arc031/tasks/arc031_2