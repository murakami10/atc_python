import itertools

for i in itertools.combinations(range(5), 2):  #nC2
    print(i[0], i[1])

'''
0 1
0 2
0 3
0 4
1 2
1 3
1 4
2 3
2 4
3 4
'''


for i in itertools.permutations(range(5), 2):  #n!
    print(i)

'''
(0, 1)
(0, 2)
(0, 3)
(0, 4)
(1, 0)
(1, 2)
(1, 3)
(1, 4)
(2, 0)
(2, 1)
(2, 3)
(2, 4)
(3, 0)
(3, 1)
(3, 2)
(3, 4)
(4, 0)
(4, 1)
(4, 2)
(4, 3)

'''