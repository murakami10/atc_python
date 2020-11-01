

T = int(input())

count_array = []
for _ in range(T):
    string = input()
    count = 0
    i = 0
    while i < len(string):
        if string[i:i+5] == "tokyo":
            i += 5
            count += 1
        elif string[i:i+5] == "kyoto":
            i += 5
            count += 1
        else:
            i += 1
    count_array.append(count)

for i in count_array:
    print(i)

#https://atcoder.jp/contests/kupc2015/tasks/kupc2015_a