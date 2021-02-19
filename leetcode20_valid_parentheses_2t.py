class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '(':')',
            '{':'}',
            '[':']'
        }
        
        stack = []
        
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if not stack:
                    return False
                if dic[stack.pop()] != c:
                    return False
        
        if stack:
            return False
        
        return True
        