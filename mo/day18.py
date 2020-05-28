

k = 3#int(input())
n = 9#int(input())
a = [i for i in range(1,10)]	
def findSum(a,cur=0,sub_a = []):
	if len(sub_a) == k and sum(sub_a) == n:
		print(sub_a)
		
	if len(sub_a) < k:
		for i in range(cur,len(a)):
			cur += 1
			sub_a.append(a[i])
			findSum(a,cur,sub_a)
			sub_a.pop()
findSum(a)
	

