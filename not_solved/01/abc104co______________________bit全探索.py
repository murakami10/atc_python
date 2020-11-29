

D, G = map(int, input().split())

ls = [tuple(map(int, input().split())) for i in range(D)]

min_count = 0
for i in ls:
    min_count+= i[0]

for i in range(2**D):
    sum = 0
    count = 0
    max_j = -1
    for j in range(D):
        if (1<<j) & i:
            sum += ls[j][1]
            sum += ls[j][0] * (j+1)*100
            count+= ls[j][0]
        else:
            max_j = j
    
    if sum >= G:
        if count < min_count:
            min_count = count
            continue
    for i in range(1, ls[max_j][0]+1):
        sum += (max_j+1)*100
        count+=1
        if sum >= G:
            if count < min_count:
                min_count = count
                break

print(min_count)

#bit全探索
#[tuple(map(int, input().split())) for i in range(D)] tuple形式をlistに収める
#https://atcoder.jp/contests/abc104/tasks/abc104_c