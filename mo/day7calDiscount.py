def calDiscount(n):
    l = list(n)
    l.remove(l[-2])
    ans = int("".join(l))
    return ans
  
for _ in range(int(input())):
	n = input()
	if n >10:
		print(calDiscount(n))
	