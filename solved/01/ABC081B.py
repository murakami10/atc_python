

start = input()

ls = list(map(int, input().split()))
count = 0

break_flag = False

while(True):
    next_list = []
    for i in ls:
        if i%2 == 0 and i != 0:
            next_list.append(i/2)
        else:
            break_flag = True
    if break_flag:
        break
    count+=1
    ls = next_list.copy()

print(count)

#https://atcoder.jp/contests/abs/tasks/abc081_b