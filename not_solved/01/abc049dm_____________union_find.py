import collections

class UnionFind:

    def __init__(self, n):
        self._parent = [i for i in range(n+1)]
        self._height = [0] * (n+1)

    def find(self, x: int) -> int:
        x_parent = self._parent[x]

        if x_parent == x:
            return x

        parent = self.find(x_parent)
        self._parent[x] = parent
        return parent

    def same_check(self, x: int, y: int) -> bool:
        x_parent = self.find(x)
        y_parent = self.find(y)

        return x_parent == y_parent

    def unit(self, x:int, y:int):
        x_parent = self.find(x)
        y_parent = self.find(y)

        x_height = self._height[x_parent]
        y_height = self._height[y_parent]

        if x_height > y_height:
            self._parent[y_parent] = x_parent
        else:
            self._parent[x_parent] = y_parent

            if x_height == y_height:
                self._height[y_parent]+= 1

        return 

N, K, L = map(int, input().split())

uf_road  = UnionFind(N)
uf_train = UnionFind(N)

for i in range(K):
    p, q = map(int, input().split())
    uf_road.unit(p,q)

for i in range(L):
    r, s = map(int, input().split())
    uf_train.unit(r, s)

pairs = [(uf_road.find(i+1), uf_train.find(i+1)) for i in range(N)]

'''
count = collections.Counter(pairs)
'''
count = collections.defaultdict(int)
for pair in pairs:
    count[pair] += 1

ans_count = [count[pairs[i]] for i in range(N)]


for i in ans_count:
    print(i, end=' ')


#https://atcoder.jp/contests/abc049/tasks/arc065_b

#collections.Counter(a)
#collections.defaultdict(int)