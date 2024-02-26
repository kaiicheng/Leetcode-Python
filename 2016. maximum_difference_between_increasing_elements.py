from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        mx = float("-inf")
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # print("i, j: ", i, j)
                if nums[i] < nums[j]:
                    mx = max(nums[j] - nums[i], mx)
        if mx == float("-inf"):
            return -1
        else:
            return mx

def main(nums):
    result = Solution()
    print(result.maximumDifference(nums))

if __name__== "__main__" :
    nums = [7,1,5,4]
    main(nums)
