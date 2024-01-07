# prefix sum

from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        left_sum = [0]
        right_sum = [0]
        for i in range(len(nums) - 1):
            left_sum.append(left_sum[-1] + nums[i])

        for i in range(len(nums) - 1, 0, -1):
            right_sum.append(right_sum[-1] + nums[i])
        right_sum.reverse()
        # print("left_sum, right_sum: ", left_sum, right_sum)

        ans = []
        for i in range(len(left_sum)):
            ans.append(abs(left_sum[i] - right_sum[i]))
        return ans

def main(nums):
    result = Solution()
    print(result.leftRightDifference(nums))

if __name__== "__main__" :
    nums = [10,4,8,3]
    main(nums)
