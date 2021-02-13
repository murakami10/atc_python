import sys  # 再帰の制限
from collections import defaultdict
from typing import Dict
from typing import List
from typing import Tuple

sys.setrecursionlimit(10 ** 8)


def dfs(curr: int, parent: int) -> Tuple[bool, int]:
    global seen, edges
    seen[curr] = True
    flag: bool = False
    count: int = 0
    for edge in edges[curr]:
        if edge == parent:
            continue

        if seen[edge]:
            flag = True
            continue

        seen_flag_dfs, tem_count = dfs(edge, curr)
        if seen_flag_dfs:
            flag = True
        count += tem_count

    count += 1
    return flag, count


N = int(input())

edges: Dict[int, List[int]] = defaultdict(lambda: list())

for _ in range(N):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


seen: Dict[int, bool] = defaultdict(bool)
for key in edges.keys():
    seen[key] = False

ans = 0

for key in edges.keys():
    if seen[key]:
        continue
    flag, count = dfs(key, 0)
    if flag:
        ans += count
    else:
        ans += count - 1
print(ans)
