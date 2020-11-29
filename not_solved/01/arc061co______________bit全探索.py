

s=input()
l=len(s)

ans_subset=0
for i in range(2**(l-1)):
    sub_string=s[0]
    for j in range(l-1):
        if(1 << j) & i:
            ans_subset+= int(sub_string)
            sub_string = s[j+1]
        else:
            sub_string+= s[j+1]
        if j == l-2:
            ans_subset+= int(sub_string)

if l == 1:
    print(s)
else:
    print(ans_subset)



#bit全探索
#https://atcoder.jp/contests/arc061/tasks/arc061_a