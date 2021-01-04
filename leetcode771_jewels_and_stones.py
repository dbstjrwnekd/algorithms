class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = collections.Counter(stones)
        count = 0
        for jewel in jewels:
            count += freq[jewel]
        
        return count