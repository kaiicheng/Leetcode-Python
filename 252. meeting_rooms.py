import copy
from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals_sorted = copy.deepcopy(intervals)
        intervals_sorted.sort(key=lambda intervals_sorted: intervals_sorted[0])
        # print(intervals_sorted)

        for i in range(len(intervals_sorted) - 1):
            if intervals_sorted[i][1] > intervals_sorted[i + 1][0]:
                return False
        return True

def main(intervals):
    result = Solution()
    print(result.canAttendMeetings(intervals))

if __name__== "__main__" :
    intervals = [[0,30],[5,10],[15,20]]
    main(intervals)
