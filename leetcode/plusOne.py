'''66.  Plus One
Easy

1362

2198

Add to List

Share
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.'''

digit = [4,3,9]
if digit[-1] < 9 :
    digit[len(digit)-1] +=1
    print(digit)
     
if digit[-1] == 9:
    num =''
    for i in digit:
        num += str(i)

    num = str(int(num)+1)
    new = []
    for i in range(len(num)):
        new.append(int(num[i]))
    print(new)
