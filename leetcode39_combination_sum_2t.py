class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answers = []
        
        candidates.sort()
        
        def dfs(comb,sub_sum=0):
            if sub_sum == target:
                answer = sorted(comb)
                if not answer in answers:
                    answers.append(answer)
            elif sub_sum < target:
                for c in candidates:
                    if sub_sum + c > target:
                        break
                    dfs(comb+[c],sub_sum+c)
        
        dfs([])
        
        return answers