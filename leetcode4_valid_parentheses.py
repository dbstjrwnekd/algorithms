class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        #validate check with stack
        for c in s:
            #if closed parentheses check the stack
            if not c in dic:
                stack.append(c)
            elif not stack or dic[c] != stack.pop():
                return False
        #check stack whether it's empty or not
        return len(stack) == 0
        