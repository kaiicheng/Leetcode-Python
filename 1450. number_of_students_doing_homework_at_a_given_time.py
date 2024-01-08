from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and queryTime <= endTime[i]:
                count += 1
        return count

def main(startTime, endTime, queryTime):
    result = Solution()
    print(result.busyStudent(startTime, endTime, queryTime))

if __name__== "__main__" :
    startTime = [1,2,3]
    endTime = [3,2,7]
    queryTime = 4
    main(startTime, endTime, queryTime)
