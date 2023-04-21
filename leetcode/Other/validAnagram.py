'''
242. Valid Anagram
Easy

1359

135

Add to List

Share
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
'''
def anagram(s,t):
    str3=sorted(s)
    str4=sorted(t)
    if str3==str4:
        print("true")
    else:
        print("false")
list1="rat"
list2="car"
anagram(list1,list2)