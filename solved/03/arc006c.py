import copy
import collections

N = int(input())

rows = [int(input())]
boxs = [int(input()) for i in range(N-1)]

for box in boxs[:]:
    for i in range(len(rows)):

        if rows[i] >= box:
            rows[i] = box
            break

        if i == len(rows) -1:
            rows.append(box)
            break


print(len(rows))

#https://atcoder.jp/contests/arc006/tasks/arc006_3