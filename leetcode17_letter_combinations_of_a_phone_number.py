class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {
            '1': [],
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        
        answer = []
        if not digits:
            return answer
        
        def dfs(index=0,discovered=''):
            if len(discovered) == len(digits):
                answer.append(discovered)
                return
            
            for i in range(index,len(digits)):
                for char in num_dict[digits[i]]:
                    dfs(i+1,discovered+char)
        
        dfs(0,'')
        
        return answer