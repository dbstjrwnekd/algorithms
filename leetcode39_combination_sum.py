class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def comb(discovered, index,candi_sum):
            for i in range(index,len(candidates)):
                discovered.append(candidates[i])
                candi_sum += candidates[i]
                if candi_sum==target: answer.append(discovered[:])
                elif candi_sum < target: comb(discovered,i,candi_sum)
                candi_sum-=discovered.pop()
        comb([],0,0)
        return answer