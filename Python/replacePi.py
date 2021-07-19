def replacePi(s):
    if(len(s) <= 2):
        return s
    if(s[0] == "p" and s[1] == "i"):
        print("3.14",end='')
        replacePi(s[2:])
    else :
        print(s[0],end="")
        replacePi(s[1:])

s = input()
replacePi(s)