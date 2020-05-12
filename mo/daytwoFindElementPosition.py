a = input().split()
b = input().split()
c = []
for _ in range(len(a)): c.append(-1)
for i in range(len(a)):
	for j in range(len(b)):

		if a[i] == b[j]:
			c[i] = j 
	
print(c)