'''In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
'''

s = input()
sub_string = input()
count = 0
x = 0
for i in range(len(s)):
	x = s.find(sub_string,x,len(s))
	
	if x >= 0 :
		count += 1
		x += 1
print(count)


	
