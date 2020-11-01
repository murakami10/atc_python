
def purse_sum(i):
    total = 0
    for s in str(i):
        total+= int(s)
    return total

N, A, B = map(int, input().split())
sum = 0
for i in range(N+1):
    """
    ls = []
    tmp_i = i
    while(True):
        if tmp_i == 0:
            break
        ls.append(tmp_i%10)
        #tmp_i= int(tmp_i /10)
        tmp_i//=10
    tmp_sum = 0
    for j in ls:
        tmp_sum+=j
    """
    tmp_sum = purse_sum(i)
    if A <= tmp_sum and tmp_sum <= B:
        sum+=i

print(sum)

#https://atcoder.jp/contests/abs/tasks/abc083_b

