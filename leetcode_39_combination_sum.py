class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        
        def dfs(found, start, temp_sum):
            if temp_sum > target:
                return
            if temp_sum == target:
                answer.append(found[:])
                return
                
            for i in range(start, len(candidates)):
                found.append(candidates[i])
                dfs(found, i, temp_sum + candidates[i])
                found.pop()
                
        dfs([], 0, 0)
        
        return answer
    