a = input().split()
j = 0
while j < len(a):
	for i in range(len(a)):
		if a[j][0] > a[i][0]:
			a[j],a[i] = a[i],a[j]
			print(a[i])

	j += 1
for i in a:
	print(i,end = '')
