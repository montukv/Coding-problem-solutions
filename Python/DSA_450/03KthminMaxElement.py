# Kth smallest element 
# Input:
# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# Output : 7
# Explanation :
# 3rd smallest element in the given 
# array is 7.


k = int(input())
arr = list(map(int,input().split()))
arr.sort()
print("\n")
print("{k}th min element is : ",arr[k-1])
print("{k}th max element is : ",arr[-k])

