from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
        mi = float("inf")
        # l = 0
        # while l < len()
        #     for i in range(len(nums) - 2):
        #         print("i, nums[i]: ", i, nums[i])

        for i in range(len(nums)):        
            for j in range(i + 1, len(nums)):        
                for k in range(j + 1, len(nums)):
                    # print("i, j, k: ", i, j, k)
                    # print("nums[i], nums[j], nums[k]: ", nums[i], nums[j], nums[k])
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        mi = min(mi, nums[i] + nums[j] + nums[k])
        # print("mi: ", mi)
        if mi == float("inf"):
            return -1
        else:
            return mi

def main(nums):
    result = Solution()
    print(result.minimumSum(nums))

if __name__== "__main__" :
    nums = [8,6,1,5,3]
    main(nums)
