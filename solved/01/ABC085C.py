
X, Y = map(int, input().split())

ten = 0
five = 0
break_flag = False
while ten*10000 <= Y or ten <= X:
    five = 0
    while ten * 10000 + five * 5000 <= Y or ten + five <= X:
        one = X - ten - five
        if(ten*10000 + five*5000 + one*1000 == Y):
            break_flag = True
            break
        five+=1
    if break_flag:
        break
    ten+=1

if break_flag:
    print("{} {} {}".format(ten, five, one))
else:
    print("-1 -1 -1")

#https://atcoder.jp/contests/abs/tasks/abc085_c