# Approach 1: Brute Force

# Intuition
# The most naive way to tackle this problem is to go through each element in nums, and for each element, consider the product of every a contiguous subarray 
# starting from that element. This will result in a cubic runtime.

# We can improve the runtime from cubic to quadratic by removing the innermost for loop in the above pseudo code. Rather than calculating the product of every 
# contiguous subarray over and over again, for each element in nums (the outermost for loop), we accumulate the products of contiguous subarrays starting 
# from that element to subsequent elements as we go through them (the second for loop). By doing so, we only need to multiply the current number with accumulated 
# product to get the product of numbers up to the current number.

# Complexity Analysis
# Time complexity : O(N^2) where NNN is the size of nums. Since we are checking every possible contiguous subarray following every element in nums we have 
# quadratic runtime

# Space complexity: O(1)
# Space complexity : O(1) since we are not consuming additional space other than two variables: result to hold the final result and accu to accumulate 
# product of preceding contiguous subarrays.


from typing import List
import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # the case that nums is empty
        if len(nums) == 0:
            return 0

        # start from nums[0]
        result = nums[0]

        # loop starting from i-th number
        for i in range(len(nums)):

            # necessary in order to maintain the later loop
            accu = 1
            
            # multiple from i-th to j-th number 
            for j in range(i, len(nums)):
                accu *= nums[j]
                result = max(result, accu)

        return result

def main():
    nums = [2,3,-2,4]
    result = Solution()
    print(result.maxSubArray(nums))


if __name__== "__main__" :
    main()