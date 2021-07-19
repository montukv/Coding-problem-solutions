#Reverse the input array
# input : {5,4,3,2,1}
# output : {1,2,3,4,5}

#Reverse the input array
# input : {5,4,3,2,1}
# output : {1,2,3,4,5}

arr = list(map(int,input().split()))
i = 0
j = len(arr)-1
while(i < j):
    arr[i],arr[j] = arr[j],arr[i]
    i += 1
    j -= 1

print(arr)