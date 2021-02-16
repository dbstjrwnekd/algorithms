class Solution:
    def sort_condition(self, point):
        return (point[0]-0)**2 + (point[1]-0)**2
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=self.sort_condition)[:K]