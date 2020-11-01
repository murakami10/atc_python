import itertools

for i in itertools.combinations(range(5), 2):  #nC2
    print(i[0], i[1])

for i in itertools.permutations(range(5), 2):  #n!
    print(i)