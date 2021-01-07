class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_courses = collections.defaultdict(list)
        for course, pre in prerequisites:
            pre_courses[course].append(pre)
        
        traced = set()
        visited = set()
        def dfs(course):
            if course in traced: return False
            if course in visited: return True
            traced.add(course)
            for pre in pre_courses[course]:
                if not dfs(pre): return False
            traced.remove(course)
            visited.add(course)
            return True
        
        for course in list(pre_courses):
            if not dfs(course):
                return False
        return True