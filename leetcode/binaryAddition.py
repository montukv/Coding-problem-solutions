
'''67. Add Binary
Easy

1589

262

Add to List

Share
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"'''


a= input('')
b= input('')
c=int(a,2)
d=int(b,2)
e=c+d
f=bin(e).replace("0b","")
print(f)