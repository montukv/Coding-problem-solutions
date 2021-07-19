# Kadane's Algorithm 
# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
# Input:
# N = 5
# arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which 
# is a contiguous subarray.


def kadenesAlgo(arr):
    max_sum = 0
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        max_sum = max(cur_sum,max_sum)
        if(cur_sum < 0):
            cur_sum = 0
    print(max_sum)
            
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
arr2 = [1,2,3,-2,5]

kadenesAlgo(arr)
kadenesAlgo(arr2)

    

