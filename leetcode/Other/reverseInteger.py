'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''

n = int(input("\nEnter a number : "))
rev = 0
while n != 0 :
	x = rev + n % 10
	n = n//10
	if n > 0:
		rev = x *10
print(x)


	
	
