import copy

N, K = map(int, input().split())
s = list(input())
s_sort = sorted(s)

count = 0
ans = ""

for i in range(N):
    for j in s_sort:

        if j == s[i]:
            tmp = 0
        else:
            tmp = 1
        
        tmp_s = s_sort[:]
        tmp_s.remove(j)
        for k in range(i+1, N):
            if s[k] in tmp_s:
                tmp_s.remove(s[k])
            else:
                tmp += 1
        if count + tmp <= K:
            ans += j
            s_sort.remove(j)
            if j != s[i]:
                count += 1
            break

print(ans)

#https://atcoder.jp/contests/abc009/tasks/abc009_3
#https://yottagin.com/?p=7373 参考