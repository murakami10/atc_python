import heapq

def calc_time(ls: list, num: int) -> int:
    ans = 0

    for _ in range(num):
        tmp_tuple = heapq.heappop(ls)
        ans += tmp_tuple[0]
        tmp_tuple[0] += tmp_tuple[1]
        heapq.heappush(ls, tmp_tuple)

    return ans

N, K = map(int, input().split())

machine = []

for i in range(N):
    a, b = map(int, input().split())
    heapq.heappush(machine, [a, b])

ans = calc_time(machine, K)

print(ans)

# https://atcoder.jp/contests/code-thanks-festival-2017-open/tasks/code_thanks_festival_2017_c