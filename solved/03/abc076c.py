import copy

s = input()
t = input()

num = len(s) -len(t)

while num >= 0:
    if s[num] == t[0] or s[num] == '?':
        i = 0
        copy_s = copy.copy(s)
        while i < len(t):
            if s[num+i] != t[i] and s[num+i] != '?':
                break
            copy_s = copy_s[:num+i] + t[i] + copy_s[num+i+1:]  #文字を置換する方法はないがスライスをすることで、イミュータブルを変更できる
            i += 1
        if i == len(t):
            break
    num -= 1
else:
    print('UNRESTORABLE')
    exit()


print(copy_s.replace('?', 'a'))

#copy_s[num+i] = copy_s[:num+i] + t[i] + copy_s[num+i:]  #文字を置換する方法はないがスライスをすることで、イミュータブルを変更できる
#文字列のreplace
#https://atcoder.jp/contests/abc076/tasks/abc076_c