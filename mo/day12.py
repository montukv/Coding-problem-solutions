
l = [5,4,3,2]#input().split()
sl = sorted(l)
count = 0
while sl!=l:
    for i in range(1,len(l)):
        if l[i-1] > l[i]:
            l[i-1],l[i] = l[i],l[i-1]
            count += 1

print(count)        
