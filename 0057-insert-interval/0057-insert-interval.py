class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left_intervals = []
        right_intervals = []
        
        for i in range(len(intervals)):
            if intervals[i][0] < newInterval[0] and intervals[i][1] < newInterval[0]:
                left_intervals.append(intervals[i])
                
            elif intervals[i][0] > newInterval[1] and intervals[i][1] > newInterval[1]:
                right_intervals.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0],intervals[i][0])
                newInterval[1] = max(newInterval[1],intervals[i][1])
                
        return left_intervals + [newInterval] + right_intervals