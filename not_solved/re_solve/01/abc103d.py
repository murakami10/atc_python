
N, M = map(int, input().split())

bridges = [list(map(int, input().split())) for _ in range(M)]

bridges.sort(key=lambda ls: ls[0])

count = 0
right_min = bridges[0][1]
right_max = bridges[0][1]

for bridge in bridges:
    if bridge[0] >= right_min:
        count += 1
        right_min = bridge[1]
        right_max = bridge[1]
    else:
        right_min = min(right_min, bridge[1])
        right_max = max(right_max, bridge[1])

print(count+1)
