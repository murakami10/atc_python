import math

def get_distance(x1, y1, x2, y2):
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return distance


N = int(input())

x = list()
y = list()
for i in range(N):
    x1, y1 = map(int, input().split())
    x.append(x1)
    y.append(y1)

max_dis = get_distance(x[0], y[0], x[1], y[1])
for i in range(N):
    for j in range(i+1, N):
        dis = get_distance(x[i], y[i], x[j], y[j])

        if max_dis < dis:
            max_dis = dis

print(max_dis)

#range(i, j) i　<= x < j を取る
# import math       math.sqrt() 平方根を取得
#https://atcoder.jp/contests/arc004/tasks/arc004_1