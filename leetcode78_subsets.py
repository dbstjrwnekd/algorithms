class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(index: int, discovered: List[int]):
            answer.append(discovered[:])
            for i in range(index,len(nums)):
                discovered.append(nums[i])
                dfs(i+1,discovered)
                discovered.pop()
        dfs(0,[])
        return answer