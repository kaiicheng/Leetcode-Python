from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        ans = -1
        mx = max(nums)
        mi = min(nums)
        for i in range(len(nums)):
            if nums[i] != mx and nums[i] != mi:
                ans = nums[i]
                break
        return ans

def main(nums):
    result = Solution()
    print(result.findNonMinOrMax(nums))

if __name__== "__main__" :
    nums = [3,2,1,4]
    main(nums)
