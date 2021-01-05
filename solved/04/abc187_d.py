import heapq

N = int(input())

a_sum = 0

heap = []

for _ in range(N):
    a, b = map(int, input().split())
    a_sum += a
    heapq.heappush(heap, -(b+a*2))


b_sum = 0
count = 0
while heap:
    top = heapq.heappop(heap)
    b_sum += -top
    count += 1
    if a_sum < b_sum:
        break

print(count)

# https://atcoder.jp/contests/abc187/tasks/abc187_d
