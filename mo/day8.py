l = input().split()
th = len(l)/4
def maxOcr(l):
	count = 0
	key = l[0]
	for i in l[1:]:
		if i == key:
			count += 1
		else: 
			key = i
			count = 0
		if count > th:
			return i


print(maxOcr(l))
