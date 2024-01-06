from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        result = float('inf')
        left = 0
        for right in range(k - 1, len(nums)):
            # print("left, right: ", left, right)
            result = min(result, nums[right] - nums[left])
            left += 1
        return result



        # wrong

        # # print("len(nums): ", len(nums))
        # if len(nums) == 1:
        #     return 0

        # for i in range(len(nums) - k):
        #     print("i: ", i)
        #     nums.remove(max(nums))
        
        # print("nums: ", nums)

        # mx = max(nums)
        # nums.remove(mx)
        # # print("nums: ", nums)
        # mi = max(nums)

        # return mx - mi
        # # return -1



        # wrong

        # # print("len(nums): ", len(nums))
        # if len(nums) == 1:
        #     return 0

        # mx = max(nums)
        # nums.remove(mx)
        # # print("nums: ", nums)
        # mi = max(nums)

        # return mx - mi

def main(nums, k):
    result = Solution()
    print(result.minimumDifference(nums, k))

if __name__== "__main__" :
    nums = [9,4,1,7]
    k = 2
    main(nums, k)
