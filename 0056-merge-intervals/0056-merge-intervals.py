class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        result = [intervals[0]]
        
        for start,end in intervals[1:]:
            endVal = result[-1][1]
            if endVal >= start:
                result[-1][1] = max(endVal,end)
            else:
                result.append([start,end])
        return result
                
        