
n = int(input())

ls = [500, 100, 50, 10, 5, 1]
count = 0

rest = 1000 - n

for i in ls:
    count = count + (rest // i)
    rest %= i

print(count)

#https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_a