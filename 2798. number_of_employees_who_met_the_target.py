from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
        ans = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                ans += 1
        return ans

def main(hours, target):
    result = Solution()
    print(result.numberOfEmployeesWhoMetTarget(hours, target))

if __name__== "__main__" :
    hours = [0,1,2,3,4]
    target = 2
    main(hours, target)
