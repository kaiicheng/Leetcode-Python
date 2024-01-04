from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        left = min(nums) + k
        right = max(max(nums) - k, left)

        return right - left



        # wrong

        # mx = max(nums)
        # mi = min(nums)
        # print("mx, mi: ", mx, mi)

        # if mx == mi:
        #     return 0

        # gap = mx - mi
        # if -1 * k < gap and gap < k:
        #     return 0
        # else:
        #     return 

def main(nums, k):
    result = Solution()
    print(result.smallestRangeI(nums, k))

if __name__== "__main__" :
    nums = [1,3,6]
    k = 3
    main(nums, k)
