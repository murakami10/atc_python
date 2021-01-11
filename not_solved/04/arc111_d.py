from typing import Dict, List, Tuple
import collections
import sys  # 再帰の制限

sys.setrecursionlimit(10 ** 8)


def dfs(curr: int, parent: int) -> Tuple[int, bool]:
    global edge, seen
    seen[curr] = 1
    flag: bool = False
    tmp_flag: bool = False
    count: int = 1
    tmp_count: int = 0
    for e in edge[curr]:
        if parent == e:
            continue

        if seen[e] != 0:
            tmp_flag = True
        else:
            tmp_count, tmp_flag = dfs(e, curr)
            count += tmp_count

        if tmp_flag:
            flag = True

    return count, flag


N = int(input())

edge: Dict[int, List[int]] = collections.defaultdict(lambda: list())
seen: Dict[int, int] = collections.defaultdict(lambda: 0)

for _ in range(N):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
    seen[a] = 0
    seen[b] = 0

ans: int = 0
for e in edge.keys():
    if seen[e] != 0:
        continue
    count, flag = dfs(e, 0)
    if not flag:
        count -= 1
    ans += count

print(ans)
# https://atcoder.jp/contests/arc111/tasks/arc111_b
