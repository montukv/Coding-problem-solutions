
def check(s,f,l):
    for i in range(len(s)):
        if s[i] == f:
            return True
        if s[i] == l :
            return False



s = str(input())
f = str(input())
l = str(input())

print(check(s,f,l))