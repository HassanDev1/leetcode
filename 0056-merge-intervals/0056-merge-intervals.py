class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for i in range(len(intervals)):
            
            
            if not merged or merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                merged[-1][0] = min(intervals[i][0],merged[-1][0])
                merged[-1][1] = max(intervals[i][1],merged[-1][1])
                
            
                
        return merged