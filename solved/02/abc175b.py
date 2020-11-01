
N = int(input())
ls = list(map(int, input().split()))
ls.sort()

if len(ls) < 3:
    print(0)
    exit()

count = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):

            #if (ls[i] + ls[j] > ls[k]) and (ls[i] != ls[j]) and (ls[j] != ls[k]) and (ls[k]!= ls[i]):
            if(ls[i] + ls[j] > ls[k]) and len(set([ls[i], ls[j], ls[k]]))==3:
                count+=1

print(count)