
class UnionFind:

    def __init__(self, n):
        self._parent = [i for i in range(n+1)]
        self._height = [0] * (n+1)

    def find(self, x: int) -> int:

        parent = self._parent[x]
        if parent == x:
            return x

        parent = self.find(parent)
        self._parent[x] = parent
        return parent

    def unit(self, x: int, y: int):
        x_parent = self.find(x)
        y_parent = self.find(y)

        x_height = self._height[x_parent]
        y_height = self._height[y_parent]

        if x_height > y_height:
            self._parent[y_parent] = x_parent
        else:
            self._parent[x_parent] = y_parent
            if x_height == y_height:
                self._height[y_parent] += 1
        return

    def same_check(self, x: int, y: int) -> bool:
        x_parent = self.find(x)
        y_parent = self.find(y)
        return x_parent == y_parent

N, Q = map(int, input().split())

uf = UnionFind(N)
for i in range(Q):
    P,A,B = map(int, input().split())
    if not P:
        uf.unit(A,B)
    else:
        if uf.same_check(A,B):
            print('Yes')
        else:
            print('No')

#https://atcoder.jp/contests/atc001/tasks/unionfind_a