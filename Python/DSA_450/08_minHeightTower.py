# Minimize the Heights II 
# Medium Accuracy: 28.62% Submissions: 100k+ Points: 4
# Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer. 
# Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.

# A slight modification of the problem can be found here.


# Example 1:

# Input:
# K = 2, N = 4
# Arr[] = {1, 5, 8, 10}
# Output:
# 5
# Explanation:
# The array can be modified as 
# {3, 3, 6, 8}. The difference between 
# the largest and the smallest is 8-3 = 5.


def minHeight(arr,k,n):

    avg = sum(arr)/n
    for i in range(n):
        if(arr[i] > avg):
            arr[i] -= k
        elif (arr[i] < avg):
            arr[i] += k
    
    difference = max(arr) - min(arr)
    print(difference)

k,n = input().split()
arr = list(map(int,input().split()))
k = int(k)
n = int(n)
minHeight(arr,k,n)
