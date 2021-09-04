import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numSet = collections.defaultdict(int)
        for num in nums:
            numSet[num] += 1
        return sorted(numSet.keys(), key=lambda x : numSet[x], reverse=True)[:k]
        