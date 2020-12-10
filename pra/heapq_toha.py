import heapq

ls = [2, 6, 7, 3, 19, 22, 20, 3, 5]
heapq.heapify(ls)

print(heapq.heappop(ls))
print(heapq.heappop(ls))
print(ls)

heapq.heappush(ls, 3)
print(ls)
heapq.heappush(ls, 15)

print(heapq.heappop(ls))
