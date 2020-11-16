

n, d = map(int, input().split())

count2 = 0
count3 = 0
count5 = 0

while d%2 == 0:
    d /= 2
    count2 += 1

while d%3 == 0:
    d /= 3
    count3 += 1

while d%5 == 0:
    d /= 5
    count5 += 1

if d != 1:
    print('0')
    exit()

ans = [[[[0] * (count5+1) for _ in range(count3+1)] for _ in range(count2+1)] for _ in range(n+1)]

ans[0][0][0][0] = 1

param2 = [0,1,0,2,0,1]
param3 = [0,0,1,0,0,1]
param5 = [0,0,0,0,1,0]

for i in range(n):
    for j in range(6):
        for c2 in range(count2+1):
            for c3 in range(count3+1):
                for c5 in range(count5+1):
                    ac2 = min(count2, c2+param2[j])
                    ac3 = min(count3, c3+param3[j])
                    ac5 = min(count5, c5+param5[j])
                    ans[i+1][ac2][ac3][ac5] += ans[i][c2][c3][c5]/6

print(ans[-1][-1][-1][-1])

#https://atcoder.jp/contests/tdpc/tasks/tdpc_dice