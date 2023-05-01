# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l1 = list(s)
        subs = []
        max_len = 0 
        for i in l1:
            if i in subs:
                while i in subs:
                    subs.pop(0)
                subs.append(i)
            else:
                subs.append(i)
            if max_len < len(subs):
                    max_len = len(subs)
        return max_len