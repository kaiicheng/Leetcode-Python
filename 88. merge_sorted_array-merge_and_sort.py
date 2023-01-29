"""
Approach 1: Merge and sort

Intuition

A naive approach would be to simply write the values from nums2 into the end of nums1, and then sort nums1. Remember that we do not need to return a value, as we should modify nums1 
in-place. While straightforward to code, this approach has a high time complexity as we're not taking advantage of the existing sorting.



Complexity Analysis

Time complexity: O((n+m)log⁡(n+m)).

The cost of sorting a list of length x using a built-in sorting algorithm is O(xlog⁡x). Because in this case we're sorting a list of length m+n, we get a total time complexity of O((n+m)log⁡(n+m)).

Space complexity: O(n), but it can vary.

Most programming languages have a built-in sorting algorithm that uses O(n) space.
"""

from typing import List

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Write the elements of num2 into the end of nums1.
        for i in range(n):
            nums1[i + m] = nums2[i]

            # print(nums1)  # [1, 2, 3, 2, 5, 6]
            # print(nums2)

        # Sort nums1 list in-place.
        nums1.sort()

def main():

    nums1, m = [1,2,3,0,0,0], 3
    nums2, n = [2,5,6], 3

    result = Solution()
    result.merge(nums1, m, nums2, n)
    print(nums1)


if __name__== "__main__" :
    main()