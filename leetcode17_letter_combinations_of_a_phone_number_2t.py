class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        num_to_al = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        
        output = []
        
        def dfs(index,discovered=''):
            if len(discovered) == len(digits):
                output.append(discovered)
                return
            
            for c in num_to_al[digits[index]]:
                dfs(index+1,discovered+c)
        
        dfs(0)
        
        return output