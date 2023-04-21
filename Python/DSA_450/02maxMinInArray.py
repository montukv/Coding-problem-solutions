# Maximum and minimum of an array using minimum number of comparisons

arr = list(map(int,input().split()))
min_ele = 999999999
max_ele = -999999

#time complexityO(n)
for i in range(len(arr)):
    max_ele = max(max_ele,arr[i])
    min_ele = min(min_ele,arr[i])

print(min_ele," \n \n",max_ele)