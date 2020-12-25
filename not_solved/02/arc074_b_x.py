import heapq
N = int(input())

ls = list(map(int, input().split()))

ans = -1*float('inf')

first_ls = ls[0:N]
S = [0] * (N+1)
heapq.heapify(first_ls)
S[0] = sum(first_ls)

for i in range(N):
    if first_ls[0] < ls[N+i]:
        S[i+1] = S[i] + (ls[N+i] - first_ls[0])
        heapq.heappop(first_ls)
        heapq.heappush(first_ls, ls[N+i])
    else:
        S[i+1] = S[i]

last_ls = list(map(lambda x: -x, ls[2*N:3*N]))
T = [0] * (N+1)
heapq.heapify(last_ls)
T[N] = sum(last_ls)

for i in range(N):
    if last_ls[0] < -1*ls[2*N-(i+1)]:
        T[N-(i+1)] = T[N-i] + (-1*ls[2*N-(i+1)] - last_ls[0])
        heapq.heappop(last_ls)
        heapq.heappush(last_ls, -1*ls[2*N-(i+1)])
    else:
        T[N-(i+1)] = T[N-i]

ans = -1*float('inf')

for i in range(N+1):
    ans = max(S[i] + T[i], ans)

print(ans)

# https://atcoder.jp/contests/arc074/tasks/arc074_b

''' ギリギリ間に合わない
import heapq, copy


N = int(input())

ls = list(map(int, input().split()))


ans = -1*float('inf')

for i in range(N+1):
    first_ls = copy.copy(ls[0:N+i])
    last_ls = list(map(lambda x: -x, ls[N+i:3 * N]))
    heapq.heapify(first_ls)
    heapq.heapify(last_ls)
    for j in range(i):
        heapq.heappop(first_ls)
    for j in range(N-i):
        heapq.heappop(last_ls)
    ans = max(sum(first_ls) + sum(last_ls), ans)


print(ans)
'''