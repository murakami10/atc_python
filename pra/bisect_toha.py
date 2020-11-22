import bisect

# bisect_leftの使い方
A = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
print(A)
index = bisect.bisect_left(A, 3)
A.insert(index, 3)
print(A)

# 探索範囲を絞り込む
A = [1, 2, 3, 3, 3, 0, 0, 0, 0, 0, 0]
index = bisect.bisect_left(A, 3, 0, 5)
print(index) # 2

# bisect_right
A = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
print(A)
print(bisect.bisect_right(A, 3))

# bisectはbisect_rightのalias

# bisect.insort_left
A = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
bisect.insort_left(A,3)
print(A)
# bisect.insort_right
# bisect.insortはrightのalias


