class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        
        def dfs(found, start):
            if len(found) == k:
                answer.append(found[:])
                return
            
            for i in range(start, n+1):
                found.append(i)
                dfs(found, i+1)
                found.pop()
            
        dfs([], 1)
            
        return answer
