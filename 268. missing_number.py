from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # gauss' formula

        # expected_sum = len(nums)*(len(nums)+1)//2
        # actual_sum = sum(nums)
        # return expected_sum - actual_sum



        # sort
        nums.sort()

        # to avoid situation when the index is 0 or -1
        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        for i in range(len(nums)):
            # print(i)
            if nums[i] != i:
                return i

def main(nums):
    result = Solution()
    print(result.missingNumber(nums))

if __name__== "__main__" :
    nums = [9,6,4,2,3,5,7,0,1]
    main(nums)
