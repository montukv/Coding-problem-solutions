l = [2,7,4,1,8,1]
l.sort()
x,y = 0,0
for i in range(len(l)-1,0,-1):
	#print(l)
	l[i-1] = l[i]-l[i-1]
	l.remove(l[i])
	l.sort()


print(l[0])

	
	


