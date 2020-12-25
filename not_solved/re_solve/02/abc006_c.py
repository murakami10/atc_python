
import bisect


N = int(input())
cards = [0]

for _ in range(N):
    c = int(input())
    left = bisect.bisect_left(cards, c)
    if left >= len(cards):
        cards.append(c)
    else:
        cards[bisect.bisect_left(cards, c)] = c


print(N - (len(cards)-1))


# https://atcoder.jp/contests/abc006/tasks/abc006_4