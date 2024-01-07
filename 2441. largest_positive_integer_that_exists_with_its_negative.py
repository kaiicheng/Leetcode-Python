from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        nums.sort()
        mx = -1
        for i in range(len(nums) - 1, -1, -1):
            # print("i: ", i)
            if (nums[i] * -1) in nums:
                mx = max(mx, nums[i])
        return mx

def main(nums):
    result = Solution()
    print(result.findMaxK(nums))

if __name__== "__main__" :
    nums = [-1,10,6,7,-7,1]
    main(nums)
