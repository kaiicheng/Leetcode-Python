from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        pre_sum = nums[0]
        for i in range(1, len(nums)):
            # print("pre_sum: ", pre_sum)
            temp = nums[i]
            nums[i] = nums[i] + pre_sum
            pre_sum += temp

        return nums

def main(nums):
    result = Solution()
    print(result.runningSum(nums))

if __name__== "__main__" :
    nums = [1,1,1,1,1]
    main(nums)
