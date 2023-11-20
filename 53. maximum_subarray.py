from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # [-2,1,-3,4,-1,2,1,-5,4]

        max_sum=nums[0]
        cur_sum=0
        # print("max_sum: ", max_sum)
        # print("cur_sum: ", cur_sum)

        for i in range(len(nums)):
            # print("---------------")
            # print("nums[i]: ", nums[i])
            # print("max_sum: ", max_sum)
            # print("cur_sum: ", cur_sum)

            cur_sum+=nums[i]
            # print("cur_sum+=i: ", cur_sum)
            max_sum=max(cur_sum, max_sum)
            # print("max_sum: ", max_sum)
            cur_sum=max(0, cur_sum)
            # print("cur_sum: ", cur_sum)
            
        # print("max_sum: ", max_sum)
        return max_sum

if __name__== "__main__" :
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = Solution()
    print(result.maxSubArray(nums))