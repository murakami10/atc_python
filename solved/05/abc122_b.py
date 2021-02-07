from typing import List

S: List[str] = list(input())

ans: int = 0
count: int = 0
for s in S:
    if s in ["A", "C", "G", "T"]:
        count += 1
    else:
        ans = max(ans, count)
        count = 0
else:
    ans = max(ans, count)

print(ans)
# https://atcoder.jp/contests/abc122/tasks/abc122_b
