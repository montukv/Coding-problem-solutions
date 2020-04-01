#longest common prefix
 def longestCommonPrefix(s):
        if s == [] :
            return "" 
        else :
            try : 
                sm = min(s, key=len)
                n = len(sm)
                lp = sm[0]
                pre = ''
                flag = True
                for i in range(0,n):					
                    for j in range(0,len(s)):
                        lp = sm[i]
                        if s[j][i] != lp :
                            flag = False
                    if flag == False:
                        break ;
                    else : 
                        pre += lp
                return pre
            except Exception:
                return ""
s =  ["flower","flow","flight"]
checkSmallestLength(s)
