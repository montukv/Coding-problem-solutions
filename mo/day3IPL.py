
t = int(input())
for i in range(t):
    p,m=[int(i) for i in sinput().split()]
    if(p<m):
        print(0)
    else:
        print(" ",p-m)
