import bisect

N = int(input())
cards = [float('inf')] * N

for i in range(N):
    card = int(input())
    cards[bisect.bisect_left(cards, card)] = card

print(N - bisect.bisect_left(cards, float('inf')))

# https://atcoder.jp/contests/abc006/tasks/abc006_4