class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        front, back = 0, 0
        charSet = {}
        for i, char in enumerate(s):
            if char in charSet:
                front = charSet[char] + 1
            else:
                max_length = max(max_length, i - front + 1)
            
            charSet[char] = i
        
        return max_length
        