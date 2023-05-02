#https://leetcode.com/problems/valid-parentheses/ 

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 0:
            stack = []
            for i in s:
                if i == "(" or i == "[" or i == "{":
                    stack.append(i)
                else:
                    if len(stack) == 0:
                        return False
                    top = stack.pop()
                    if top == "(" and i != ")":
                        return False
                    if top == "[" and i != "]":
                        return False
                    if top == "{" and i != "}":
                        return False
            if len(stack) == 0:
                return True
            else:
                return False            
        return False