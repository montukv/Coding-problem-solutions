a = list(map(int,input().split()))
a.sort()
for i in range(1,len(a)):
	if a[i-1] == a[i]:
		print(a[i])
		break;