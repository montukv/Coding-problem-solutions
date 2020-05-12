a = list(map(int,input().split()))
setOfA = set(a)
if len(setOfA) > 2:
    print(list(setOfA)[-3])
else:
    print(max(a))
