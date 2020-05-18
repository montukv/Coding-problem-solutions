def cal(a,b,c):
    return b**2 - 4*a*c 

a= int(input())
b= int(input())
c = int(input())
if cal(a,b,c)>0:
    print("Two solutions ")
if cal(a,b,c)==0:
    print("one solutions" )
if cal(a,b,c)<0:
    print("no solutions ")