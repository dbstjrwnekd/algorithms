class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n==0: return []
        
        answer = []
        
        def comb(index=0,discovered=[]):
            if len(discovered)==k:
                answer.append(discovered[:])
                return
            
            for number in range(index,n):
                if not number+1 in discovered:
                    discovered.append(number+1)
                    comb(number+1)
                    discovered.remove(number+1)
        comb()
        return answer
            