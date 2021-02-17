class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_num = cookie_num = 0
        
        while child_num < len(g) and cookie_num < len(s):
            if g[child_num] <= s[cookie_num]:
                child_num+=1
            cookie_num+=1
        
        return child_num
    