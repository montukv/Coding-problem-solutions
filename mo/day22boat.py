a = list(map(int,input().split()))
t = int(input())
ans , temp = [] , []
for i in range(len(a)) :
	temp.append(a[i])
	if sum(temp) == t :
		ans.append(temp)
		temp = []
	if i+1 < len(a):
		if sum(temp)+a[i+1] > t:
			ans.append(temp)
			temp = []
	
print(len(ans),"boat",ans)
