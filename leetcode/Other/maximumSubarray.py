'''53. Maximum Subarray
Easy

7181

329

Add to List

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.'''



#solved Using kadanes 
array = list(map(int,input().split()))
ans = -99999999999999999
curr_sum = 0
for i in array:
	curr_sum += i
	ans = max(ans,curr_sum)
	curr_sum = max(curr_sum,0)

print(ans)

