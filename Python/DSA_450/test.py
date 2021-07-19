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