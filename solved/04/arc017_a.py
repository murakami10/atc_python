

N = int(input())


for i in range(2, int(pow(N, 0.5))+1):
    if N % i == 0:
        print("NO")
        exit()

print("YES")

# https://atcoder.jp/contests/arc017/tasks/arc017_1
