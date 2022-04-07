#20.Valid Parentheses
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i, k in enumerate(s):
            if k == "(" or k == "[" or k =="{":
                stack.append(k)
            elif len(stack) == 0 and (k == "}" or "]" or ")"):
                    return False
            else: 
                if k == "]" and stack[-1] != "[":
                    return False
                elif k == "}" and stack[-1] != "{":
                    return False
                elif k == ")" and stack[-1] != "(":
                    return False
                elif k == "]" and stack[-1] == "[":
                    stack.pop()
                elif k == "}" and stack[-1] == "{":
                    stack.pop()
                elif k == ")" and stack[-1] == "(":
                    stack.pop()
        return len(stack) == 0
                
