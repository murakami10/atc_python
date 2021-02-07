from typing import List

N = int(input())

S: List[int] = [int(x) for x in input()]
count: int = 0
for i1 in range(0, 10):
    for i2 in range(0, 10):
        for i3 in range(0, 10):
            i: List[int] = [i1, i2, i3]
            number: int = 0
            for s in S:
                if s == i[number]:
                    number += 1
                    if number == 3:
                        break
            else:
                continue
            count += 1
print(count)
# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
