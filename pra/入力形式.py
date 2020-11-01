
#input()は1行ずつ

#Input	            script	結果
#abcde	            s=input()	                             s='abcde'
#abcde	            s=list(input())	                         s=['a', 'b', 'c', 'd', 'e']
#5(1つだけ)	         a=int(input())	                          a=5
#1 2	            x,y = map(int,input().split())	         x=1,y=2
#1 2 3 4 5 ... n 	li = input().split()	                 li=['1','2','3',...,'n']
#1 2 3 4 5 ... n 	li = list(map(int,input().split()))	     li=[1,2,3,4,5,...,n]
#FFFTFTTFF          li = input().split('T')	                 li=['FFF', 'F', '', 'FF']

#行数指定のとき

"""
s = int(input())
string_list = [input() for i in range(s)]

print(string_list)
"""