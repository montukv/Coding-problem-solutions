num ,k = 1000000000 , 9

for i in range(int(k)):
	if num%10 == 0 :
		num = num // 10
		print("if " ,num)
	else :
		num -=1
		print("else " ,num)
print(num)

