import collections

N = int(input())

dic = collections.defaultdict(int)

for _ in range(N):
    string = input()
    dic[string] += 1

M = int(input())

for _ in range(M):
    string = input()
    dic[string] -= 1

ans = 0

for index, value in dic.items():
    ans = max(ans, value)

print(ans)

# https://atcoder.jp/contests/abc091/tasks/abc091_b
