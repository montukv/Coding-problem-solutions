def merge(arr,l,mid,r):
    n1 = mid-l+r
    n2 = r-mid

    temp1 = []
    temp2 = []

    for i in range(n1):
        temp1.append(arr[l+i])

    for i in range(n2):
        temp2.append(arr[mid+1+i])

    i = 0
    j = 0
    k = l
    while(l<n1 and r<n2):
        if(temp1[i] < temp2[j]):
            arr[k] = temp1[i]
            i+=1
        else:
            arr[k] = temp2[j]
            j += 1
        k+=1

    while(l<n1):
        arr[k] = temp1[i]
        i+= 1
        k+=1

    while(r<n2):
        arr[k] = temp2[j]
        j += 1
        k += 1   

def mergeSort(arr,l,r):
    if(l < r):
        mid = (l+r)/2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)

        merge(arr,l,mid,r)


n = int(input())
arr = list(map(int,input().split()))

mergeSort(arr,0,n-1)

print(arr)