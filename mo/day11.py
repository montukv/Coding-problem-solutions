def cal(l):
    
    ans = 1
    for i in range(len(l)):
        ans = ans*int(l[i])
    return ans


n = 832
print(cal(str(n)))
