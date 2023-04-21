# Sort an array of 0s, 1s and 2s 
# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.



arr = list(map(int,input().split()))

#Count the number of 0s 1s 2s in array and then just print all in order

zero = 0
one = 0
two = 0

for ele in arr:
    if(ele == 0):
        zero += 1
    if(ele == 1):
        one += 1
    if(ele == 2):
        two += 1
sorted_arr = []
while(zero > 0):
    sorted_arr.append(0)
    zero -= 1
while(one > 0):
    sorted_arr.append(1)
    one -= 1
while(two > 0):
    sorted_arr.append(2)
    two -= 1



print(arr)
print(sorted_arr)
