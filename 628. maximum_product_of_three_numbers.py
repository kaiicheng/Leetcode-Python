from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        maximus = float("-inf")
        nums.sort()
        maximus = max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
        return maximus



        # Time Limit Exceeded
        
        # if len(nums) == 3:
        #     return nums[0] * nums[1] * nums[2]
        # maximus = float("-inf")
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         for k in range(len(nums)):
        #             if i < j and j < k:
        #                 maximus = max(maximus, nums[i] * nums[j] * nums[k])
        # return maximus

def main(nums):
    result = Solution()
    print(result.maximumProduct(nums))

if __name__== "__main__" :
    nums = [1,2,3]
    main(nums)
