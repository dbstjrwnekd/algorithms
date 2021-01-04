class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = max_length = 0
        for i, val in enumerate(s):
            if val in used and start <= used[val]:
                start = used[val] + 1
            else:
                max_length = max(max_length,i-start+1)
            used[val] = i
        return max_length