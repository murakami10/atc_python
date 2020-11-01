
N = int(input())

ls = [int(input()) for i in range(N)]

ans_min = sum(ls)

for i in range(2**N):
    first_niku, second_niku = 0,0
    for j in range(N):
        if (1<<j) & i:
            first_niku+=ls[j]
        else:
            second_niku+=ls[j]
    minutes = max(first_niku, second_niku)
    if ans_min > minutes:
        ans_min = minutes

print(ans_min)

#https://atcoder.jp/contests/arc029/tasks/arc029_1