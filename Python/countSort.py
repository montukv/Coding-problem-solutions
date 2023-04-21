def countSortAlgo(a,n):
    #find max element of the array and create a emty array of size k
    k = max(a)+1
    count_arr = [0]*k

    #add count of each element to its index
    for i in range(n):
        count_arr[a[i]] += 1

    #modify count array with count of previous element

    for i in range(1,len(count_arr)):
        count_arr[i] += count_arr[i-1]
    

    #creating an ans array of size n
    ans = [0]*n

    #putting ith element in count_arr[a[i]-1] position (iterating backword)
    for i in range(1,n+1):
        count_arr[a[-i]] -= 1
        ans[count_arr[a[-i]]] = a[-i]
    
    print(ans)

arr = [10, 14, 28, 11, 7, 16, 30, 50, 25, 18]
countSortAlgo(arr,len(arr))



#time complexity O(max(Ai,n))