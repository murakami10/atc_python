
ls = list(input())

ans_sum = 0
length = len(ls)
for bits in range(2**(length-1)):
    tmp_sum = ls[0]
    for i in range(length-1):
        if 1 << i & bits:
            ans_sum += int(tmp_sum)
            tmp_sum = ls[i+1]
        else:
            tmp_sum += ls[i+1]
    ans_sum += int(tmp_sum)

print(ans_sum)

# https://atcoder.jp/contests/arc061/tasks/arc061_a
