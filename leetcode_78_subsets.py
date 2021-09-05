class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(index, found):
            answer.append(found[:])
            
            for i in range(index+1, len(nums)):
                dfs(i, found + [nums[i]])
        
        dfs(-1,[])
        
        return answer
        