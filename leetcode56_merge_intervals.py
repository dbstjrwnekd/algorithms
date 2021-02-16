class Solution:
    def mergeTwoList(self, L1: List[int], L2: List[int]) -> List:
        return [min(L1[0],L2[0]),max(L1[1],L2[1])]
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        answer = []
        for i in range(len(intervals)):
            if i < len(intervals)-1 and intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1] = self.mergeTwoList(intervals[i],intervals[i+1])
            else:
                answer.append(intervals[i])
        
        return answer