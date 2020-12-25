
import sys  # 再帰の制限
sys.setrecursionlimit(10**8)

def judge_nibu(curr: int, color: int) -> bool:
    global colors

    re_color = color ^ 1


    for i in edge[curr]:
        if colors[i] == color:
            return False

        elif colors[i] == -1:
            colors[i] = re_color

            if not judge_nibu(i, re_color):
                return False

        else:
            pass

    return True



N, M = map(int, input().split())

edge = [[] for _ in range(N+1)]
colors = [-1] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

colors[1] = 0
if judge_nibu(1, 0):
    num_zero, num_one = (0, 0)
    for color in colors:
        if color == 1:
            num_one += 1
        elif color == 0:
            num_zero += 1
        else:
            pass

    print(num_zero*num_one - M)
else:
    print(N*(N-1)//2 - M)


# https://atcoder.jp/contests/code-festival-2017-qualb/tasks/code_festival_2017_qualb_c

