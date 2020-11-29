import collections, copy


N, K = map(int, input().split())
S = list(input())

S_sort = copy.copy(S)
S_sort.sort()

ans = ''
count = 0

for i in range(len(S)):
    for j in S_sort:

        tmp_s = copy.copy(S_sort)
        tmp_s.remove(j)

        if S[i] == j:
            tmp_first = 0
        else:
            tmp_first = 1

        tmp = tmp_first
        for k in range(i+1, len(S)):
            if S[k] in tmp_s:
                tmp_s.remove(S[k])
            else:
                tmp += 1

        if tmp + count <= K:
            ans += j
            S_sort.remove(j)
            count += tmp_first
            break

print(ans)