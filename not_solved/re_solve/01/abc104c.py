
D, G = map(int, input().split())

scores = [list(map(int, input().split())) for _ in range(D)]


ans = float('inf')

for bit in range(1 << (D+1)):

    point = 0
    count = 0
    index_max = 0

    for i in range(D):
        if (1 << i) & bit:
            point += scores[i][1] + 100*(i+1)*scores[i][0]
            count += scores[i][0]
        else:
            index_max = i

    for i in range(scores[index_max][0]):
        if point >= G:
            ans = min(count, ans)
            break
        point += 100*(index_max+1)
        count += 1

print(ans)