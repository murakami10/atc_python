import itertools

N, M = map(int, input().split())

relationship = [[0]* N for i in range(N)]
for i in range(M):
    x,y = map(int, input().split())
    relationship[x-1][y-1] = 1
    relationship[y-1][x-1] = 1


team_num = 1
for i in range(2**N):

    make_team = True
    group = list()
    for j in range(N):
        if (1<<j) & i:
            group.append(j)
    '''
    for relation_i in range(len(group)):
        for relation_j in range(relation_i+1, len(group)):
            if relationship[group[relation_i]][group[relation_j]] != 1:
                make_team = False
    '''
    for i in itertools.combinations(group, 2):
        if relationship[i[0]][i[1]] == 0:
            make_team = False
            break

    if make_team:
        team_num = max(team_num, len(group))

print(team_num)


# 0で初期化されたN*Nのリストを作る [[0]*N for i in range(N)]
# itertools.combinations() nC2を取得する
#https://atcoder.jp/contests/abc002/tasks/abc002_4