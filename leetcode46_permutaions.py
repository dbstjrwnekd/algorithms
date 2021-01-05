class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #return list(itertools.permutations(nums))
        if not nums: return []
        
        answer = []
        def permu(discovered=[]):
            if len(discovered) == len(nums):
                answer.append(discovered[:])
                return
            
            for n in nums:
                if not n in discovered:
                    discovered.append(n)
                    permu(discovered)
                    discovered.remove(n)
        permu()
        return answer