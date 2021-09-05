class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preTable = collections.defaultdict(list)
        for cur, pre in prerequisites:
            preTable[cur].append(pre)
            
        visited = set()
        traced = set()
        
        def dfs(city):
            if city in traced:
                return False
            if city in visited:
                return True
            
            traced.add(city)
            for next_city in preTable[city]:
                if not dfs(next_city):
                    return False
            traced.remove(city)
            visited.add(city)
            return True
            
        for city in list(preTable.keys()):
            if not dfs(city):
                return False
            
        return True