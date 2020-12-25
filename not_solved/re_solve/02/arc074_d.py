import copy
import heapq

N = int(input())

ls = list(map(int, input().split()))
first = copy.copy(ls[0:N])
heapq.heapify(first)

last = copy.copy(ls[2*N:3*N])
last = list(map(lambda x: -x, last))
heapq.heapify(last)

ans = [[0]*(N+1) for _ in range(2)]
ans[0][0] = sum(first)
ans[1][-1] = sum(last)

for i in range(N):
    heapq.heappush(first, ls[N+i])
    pop = heapq.heappop(first)
    if pop == ls[N+i]:
        ans[0][i+1] = ans[0][i]
    else:
        ans[0][i+1] = ans[0][i] + ls[N+i] - pop

    heapq.heappush(last, -ls[2*N-i-1])
    pop = heapq.heappop(last)
    if pop == -ls[2*N-i-1]:
        ans[1][N-1-i] = ans[1][N-i]
    else:
        ans[1][N-1-i] = ans[1][N-i] - ls[2*N-i-1] - pop



mx = -float('inf')
for i in range(N+1):
    mx = max(mx, ans[0][i] + ans[1][i])

print(mx)