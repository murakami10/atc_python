
N = input()

ls = list(map(int, input().split()))
#ls.sort(reverse=True)
ls.sort()
ls = ls[::-1]
print(ls[:2], "\n")
"""
count = 0
for index, num in enumerate(ls):
    if index % 2 == 0:
        count += num
    else:
        count -= num
"""
count = sum(ls[::2]) - sum(ls[1::2])
print(count)

#for index, content in enumerate(list) indextとその中身を取る
# list = list[::-1] listを逆順にする
#https://atcoder.jp/contests/abs/tasks/abc088_b