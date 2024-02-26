from typing import List

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        
        nums.sort()
        # print("nums: ", nums)

        mi = float("inf")
        for i in range(1, len(nums)):
            gap = abs(nums[i] - nums[i - 1])
            mi = min(gap, mi)
        
        return mi

def main(nums):
    result = Solution()
    print(result.findValueOfPartition(nums))

if __name__== "__main__" :
    nums = [1,3,2,4]
    main(nums)
