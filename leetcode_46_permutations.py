class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        
        answer = []
        
        def dfs(found, flags):
            if len(found) == len(nums):
                answer.append(found[:])
                return
            
            for i in range(0, len(nums)):
                if not flags[i]:
                    flags[i] = True
                    dfs(found+[nums[i]], flags)
                    flags[i] = False
        
        dfs([], [False]*len(nums))
        
        return answer
        