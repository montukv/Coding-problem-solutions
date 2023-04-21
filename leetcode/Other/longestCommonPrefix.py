#longest common prefix
 def longestCommonPrefix(s):
   if not s:  
            return ""
        common = min(s,key=len) 
        for i in s:  
            while not i.startswith(common): 
                common = common[:len(common)-1]
                if not common:
                    return ""
        return common
        
s =  ["flower","flow","flight"]
checkSmallestLength(s)
