
str_list = ["dreamer", "dream", "eraser", "erase"]

S = input()

while(True):
    if S[-5:] in str_list:
        S = S[:-5]
    elif S[-6:] in str_list:
        S = S[:-6]
    elif S[-7:] in str_list:
        S = S[:-7]
    else:
        break

if len(S) == 0:
    print("YES")
else:
    print("NO")

#https://atcoder.jp/contests/abs/tasks/arc065_a