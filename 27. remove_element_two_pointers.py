"""
Summary
This is a pretty easy problem, but one may get confused by the term "in-place" and think it is impossible to remove an element from the array without making a 
copy of the array.

Hints
1. Try two pointers.
2. Did you use the fact that the order of elements can be changed?
3. What happens when the elements to remove are rare?


Solution Article

Approach 1: Two Pointers
Intuition

Since this question is asking us to remove all elements of the given value in-place, we have to handle it with O(1) extra space. How to solve it? We can 
keep two pointers iii and j, where iii is the slow-runner while j is the fast-runner.

Algorithm

When nums[j] equals to the given value, skip this element by incrementing j. As long as nums[j]≠val, we copy nums[j] to nums[i] and increment both indexes 
at the same time. Repeat the process until j reaches the end of the array and the new length is i.

This solution is very similar to the solution to Remove Duplicates from Sorted Array.



Complexity analysis

Time complexity : O(n). Assume the array has a total of nnn elements, both i and j traverse at most 2n steps.

Space complexity : O(1).
"""

from typing import List

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # nums = [0,1,2,2,3,0,4,2]
        # val = 2

        # the fisrt pointer
        i = 0

        # j is the second pointer
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
            print(nums)
        return i


def main():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = Solution()
    print(result.removeElement(nums, val))


if __name__== "__main__" :
    main()