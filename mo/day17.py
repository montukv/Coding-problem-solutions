def cal(arr,t):
	sub = []
	for i in arr:
		if sum(sub) >= t:
			return sub
		sub.append(i)

		






		

	





arr = [2,1,2,4,3,1]
t = 7
base = arr.index(max(arr))+1
l = arr[:base]
x = reversed(l)
print(x)


leftSub = cal(arr[:base],t)

