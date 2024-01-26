from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[1])
        # print("intervals: ", intervals)

        ans = 0
        k = float("-inf")

        for x, y in intervals:
            # print("x, y, k: ", x, y, k)
            if x >= k:
                # Case 1
                k = y
            else:
                # Case 2
                ans += 1
        
        return ans

def main(intervals):
    result = Solution()
    print(result.eraseOverlapIntervals(intervals))

if __name__== "__main__" :
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    main(intervals)
