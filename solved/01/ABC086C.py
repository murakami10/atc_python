
N = int(input())

pre_t, pre_x, pre_y = 0, 0, 0

for i in range(N):
    t, x, y = map(int, input().split())
    dis = abs(x - pre_x) + abs(y - pre_y)
    if t - pre_t < dis or (x+y)%2 != t%2:
        print("No")
        exit()
    pre_t, pre_x, pre_y = t, x, y
    

print("Yes")

#https://atcoder.jp/contests/abs/tasks/arc089_a