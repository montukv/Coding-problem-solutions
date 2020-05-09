def find(s):
	if s > 0 :
		for i in range(9):
			if s + i == 10:
				return i
	else :
		return 0
s = 0
t = int(input())
for _ in range(int(t)):
	n = int(input())
	f = n
	while(n>0):
	    d = n%10
	    s += d
	    n = n//10
	x = find(s)
	print(str(f)+str(x))
	d = 0
	s = 0 