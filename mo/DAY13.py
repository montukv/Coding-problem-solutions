

'''
#for custom input
l = []
n = int(input("height of triangle "))
for _ in range(n):
	sub_l = []
	sub_l = list(map(int,input().split()))
	l.append(sub_l)
'''
l = [[2],[3,4],[6,5,7],[4,1,8,3]]
ans = 0
for i in l:
	ans += min(i)
print(ans)
