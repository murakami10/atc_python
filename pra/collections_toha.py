import collections


# collections
fruits = ["apple", "banana", "apple"]

count1 = collections.defaultdict(int)

for i in fruits:
    count1[i] += 1

print(count1)

# Counter
count2 = collections.Counter(fruits)

print(count2)

# deque
queue = collections.deque([1,2,3])
print(queue)
queue.append(4)
print(queue)
queue.appendleft(0)
print(queue)
print(queue.pop())
print(queue.popleft())