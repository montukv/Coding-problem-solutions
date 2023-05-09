# https://leetcode.com/problems/group-anagrams/ 

def group_anagrams(strs):
    temp_strs = []
    if len(strs) == 1:
        return [strs] 
    for i in range(len(strs)):
        temp_strs.append(sorted(strs[i]))
    print(temp_strs)
    return strs

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))

strs = [""]
print(group_anagrams(strs))