class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key = lambda x : x[0]):
            if merged and i[0] <= merged[len(merged)-1][1]:
                merged[len(merged)-1][1] = max(i[1], merged[len(merged)-1][1])
            else:
                merged.append(i)
        return merged
        