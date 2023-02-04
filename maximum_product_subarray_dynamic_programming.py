# Approach 1: Dynamic Programming

# Intuition
# Rather than looking for every possible subarray to get the largest product, we can scan the array and solve smaller subproblems.

# Let's see this problem as a problem of getting the highest combo chain. The way combo chains work is that they build on top of 
# the previous combo chains that you have acquired. The simplest case is when the numbers in nums are all positive numbers. In that case, 
# you would only need to keep on multiplying the accumulated result to get a bigger and bigger combo chain as you progress.

# However, two things can disrupt your combo chain:
# 1. Zeros
# 2. Negative numbers

# 1. Zeros will reset your combo chain. A high score which you have achieved will be recorded in placeholder result. You will have to restart your combo chain after zero. 
# If you encounter another combo chain which is higher than the recorded high score in result, you just need to update the result.

# 2. Negative numbers are a little bit tricky. A single negative number can flip the largest combo chain to a very small number. This may sound like your combo chain has 
# been completely disrupted but if you encounter another negative number, your combo chain can be saved. Unlike zero, you still have a hope of saving your combo chain 
# as long as you have another negative number in nums (Think of this second negative number as an antidote for the poison that you just consumed). However, 
# if you encounter a zero while you are looking your another negative number to save your combo chain, you lose the hope of saving that combo chain.

# While going through numbers in nums, we will have to keep track of the maximum product up to that number (we will call max_so_far) and minimum product up to that 
# number (we will call min_so_far). The reason behind keeping track of max_so_far is to keep track of the accumulated product of positive numbers. The reason behind 
# keeping track of min_so_far is to properly handle negative numbers.

# max_so_far is updated by taking the maximum value among:
# 1. Current number.
# This value will be picked if the accumulated product has been really bad (even compared to the current number). This can happen when the current number has a 
# preceding zero (e.g. [0,4]) or is preceded by a single negative number (e.g. [-3,5]).
# 2. Product of last max_so_far and current number.
# This value will be picked if the accumulated product has been steadily increasing (all positive numbers).
# 3. Product of last min_so_far and current number.
# This value will be picked if the current number is a negative number and the combo chain has been disrupted by a single negative number before (In a sense, 
# this value is like an antidote to an already poisoned combo chain).

# min_so_far is updated in using the same three numbers except that we are taking minimum among the above three numbers.

# In the animation below, you will observe a negative number -5 disrupting a combo chain but that combo chain is later saved by another negative number -4. 
# The only reason this can be saved is because of min_so_far. You will also observe a zero disrupting a combo chain.


# Complexity Analysis
# Time complexity : O(N) where NNN is the size of nums. The algorithm achieves linear runtime since we are going through nums only once.

# Space complexity : O(1) since no additional space is consumed rather than variables which keep track of the maximum product so far, 
# the minimum product so far, current variable, temp variable, and placeholder variable for the result.


from typing import List
import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # need to think about situation when coming cross a zero or negative number

        # the case that nums is empty
        if len(nums) == 0:
            return 0

        # set up max_so_far, min_so_far, result 
        # use nums[0] as basis
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        # loop over starting from nums[1]
        for i in range(1, len(nums)):
            curr = nums[i]

            # max() can compare multiple numbers simultaneously
            # need to check the result after multipling current number
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result

def main():
    nums = [2,3,-2,4]
    result = Solution()
    print(result.maxSubArray(nums))


if __name__== "__main__" :
    main()