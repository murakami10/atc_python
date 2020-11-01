

S = input()
length = len(S)


for i in range(2**(length-1)):
    ans_subset = 0
    ans = int(S[0])
    for j in range(length-1):
        if(1<<j) & i:
            ans += int(S[j+1])
        else:
            ans -= int(S[j+1])
    if ans == 7:
        ans_subset = i
        break

ans_str = S[0]
for j in range(length-1):
    if (1<<j) & i:
        ans_str+= '+'
    else:
        ans_str+= '-'
    ans_str+= S[j+1]

print(ans_str+'=7')

#bit全探索
#https://atcoder.jp/contests/abc079/tasks/abc079_c