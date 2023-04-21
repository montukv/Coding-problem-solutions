# Move all negative numbers to beginning and positive to end with constant extra space
# Difficulty Level : Easy
# Last Updated : 09 Jun, 2021
# An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

# Examples : 

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5


arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(arr)
start = 0
end = len(arr)-1
while(start < end):
    
    while(arr[end] < 0 and end >  start):
        end -= 1
    if(arr[start] < 0):
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
    if(arr[start] >= 0):
        start += 1

print(arr)
