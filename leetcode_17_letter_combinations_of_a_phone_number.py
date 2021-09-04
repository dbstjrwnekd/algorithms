class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        dig_to_al = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def dfs(depth, found, keys):
            if depth >= len(keys):
                result.append(found)
                return
            
            for char in dig_to_al[keys[depth]]:
                dfs(depth+1, found+char, keys)
        
        dfs(0, '', digits)
        
        return result
