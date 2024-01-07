from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        pre = nums[0]
        for i in range(1, len(nums)):
            # print("i, nums[i]: ", i, nums[i])
            if pre == nums[i]:
                nums[i - 1] = nums[i - 1] * 2
                nums[i] = 0
            pre = nums[i]
        # print("nums: ", nums)
        
        ans = []
        zero = []
        for i in nums:
            if i == 0:
                zero.append(0)
            else:
                ans.append(i)

        return ans + zero



        # wrong

        # ans = []
        # zero = []

        # pre = nums[0]
        # i = 1
        # while i < len(nums) - 1:
        #     print("i, nums[i]: ", i, nums[i])
        #     if pre == nums[i]:
        #         ans.append(pre * 2)
        #         zero.append(0)
        #         i += 1
        #     else:
        #         ans.append(pre)
        #         zero.append(0)
        #     pre = nums[i]
        #     i += 1
        
        # return ans + zero

def main(nums):
    result = Solution()
    print(result.applyOperations(nums))

if __name__== "__main__" :
    nums = [1,2,2,1,1,0]
    main(nums)
