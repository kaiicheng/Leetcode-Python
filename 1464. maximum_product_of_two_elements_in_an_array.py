from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        nums.sort()
        x = 0
        if nums[0] < 0 and nums[1] < 0:
            x = (nums[0] - 1) * (nums[1] - 1)
        y = (nums[-1] - 1) * (nums[-2] - 1)
        # print("x, y: ", x, y)
        return max(x, y)

def main(nums):
    result = Solution()
    print(result.maxProduct(nums))

if __name__== "__main__" :
    nums = [3,4,5,2]
    main(nums)
