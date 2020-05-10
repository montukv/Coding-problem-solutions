'''58. Length of Last Word
Easy

586

2261

Add to List

Share
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5'''

s = 'to test this code  '
try:
    print(len(s.split()[-1]))
except IndexError:
    print(0)