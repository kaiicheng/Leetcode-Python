"""
Approach 1: Binary Search

Intuition

Based on the description of the problem, we can see that it could be a good match with the binary search algorithm.

    Binary search is a search algorithm that find the position of a target value within a sorted array.

Usually, within binary search, we compare the target value to the middle element of the array at each iteration.

    - If the target value is equal to the middle element, the job is done.

    - If the target value is less than the middle element, continue to search on the left.

    - If the target value is greater than the middle element, continue to search on the right.

Here we showcase a simple example on how it works.


 
To mark the search boundaries, one could use two pointers: left and right. Starting from left = 0 and right = n - 1, we then move 
either of the pointers according to various situations:

    While left <= right:

        - Pivot index is the one in the middle: pivot = (left + right) / 2. The pivot also divides the original array into two subarray.

        - If the target value is equal to the pivot element: target == nums[pivot], we're done.

        - If the target value is less than the pivot element target < nums[pivot], continue to search on the left subarray by moving the right pointer right = pivot - 1.

        - If the target value is greater than the pivot element target > nums[pivot], continue to search on the right subarray by moving the left pointer left = pivot + 1.

What if the target value is not found?

In this case, the loop will be stopped at the moment when right < left and nums[right] < target < nums[left]. Hence, the proper position 
to insert the target is at the index left.



Integer Overflow

Let us now stress the fact that pivot = (left + right) // 2 works fine for Python3, which has arbitrary precision integers, but it could cause some issues in Java and C++.

If left + right is greater than the maximum int value 2^31−1, it overflows to a negative value. In Java, it would trigger an exception of ArrayIndexOutOfBoundsException, 
and in C++ it causes an illegal write, which leads to memory corruption and unpredictable results.

Here is a simple way to fix it:

Python:
pivot = (left + right) // 2

and here is a bit more complicated but probably faster way using the bit shift operator.
Python:
pivot = (left + right) >> 1



Algorithm

    - Initialize the left and right pointers : left = 0, right = n - 1.

    - While left <= right:

        - Compare middle element of the array nums[pivot] to the target value target.

            - If the middle element is the target, i.e. target == nums[pivot]: return pivot.

            - If the target is not here:

                - If target < nums[pivot], continue to search on the left subarray. right = pivot - 1.

                - Else continue to search on the right subarray. left = pivot + 1.

    - Return left.



Complexity Analysis

Time complexity : O(log⁡N).
Let us compute the time complexity with the help of master theorem T(N)=aT(N/b)+Θ(N^d). The equation represents dividing the problem up into aaa subproblems of size N/b in Θ(N^d) time. 
Here at each step there is only one subproblem i.e. a = 1, its size is a half of the initial problem i.e. b = 2, and all this happens in a constant time i.e. d = 0. As a result, 
log⁡ b(a)=d and hence we're dealing with case 2 that results in O((n^log⁡b(a))(log⁡^(d+1)N)) time complexity.

Space complexity : O(1) since it's a constant space solution.
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left



def main():
    nums = [2, 0, 50, 12, 11, 15, 7]
    target = 9
    result = Solution()
    print(result.twoSum(nums, target))


if __name__== "__main__" :
    main()