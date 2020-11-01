
N, M = map(int, input().split())


pairs = [ list(map(int, input().split())) for _ in range(M)]



pairs.sort(reverse=True)

last = pairs[0][0]
cut_count = 1

for pair in pairs:
    if last >= pair[1]:
        cut_count += 1
        last =pair[0]

print(cut_count)

'''
pairs.sort()
#pairs = sorted(pairs)

cut_count = 0
i = 1
end_min = pairs[0][1]
for pair in pairs:
    if pair[0] >= end_min:
        end_min = pair[1]
        cut_count += 1
    end_min = min(end_min, pair[1])

cut_count += 1

print(cut_count)
'''

#https://atcoder.jp/contests/abc103/tasks/abc103_d