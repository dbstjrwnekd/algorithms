class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, confirmed, stack = collections.Counter(s), set(), []
        
        for char in s:
            counter[char] -= 1
            if char in confirmed:
                continue
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                confirmed.remove(stack.pop())
            stack.append(char)
            confirmed.add(char)
        
        return ''.join(stack)