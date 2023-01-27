"""
Approach 2: Two Pointers - when elements to remove are rare

Intuition

Now consider cases where the array contains few elements to remove. For example, nums=[1,2,3,5,4],val=4nums = [1,2,3,5,4], val = 4nums=[1,2,3,5,4],val=4. 
The previous algorithm will do unnecessary copy operation of the first four elements. Another example is nums=[4,1,2,3,5],val=4nums = [4,1,2,3,5], 
val = 4nums=[4,1,2,3,5],val=4. It seems unnecessary to move elements [1,2,3,5] one step left as the problem description mentions that the order of elements 
could be changed.

Algorithm

When we encounter nums[i]=valnums[i] = valnums[i]=val, we can swap the current element out with the last element and dispose the last one. This essentially reduces the array's size by 1.

Note that the last element that was swapped in could be the value you want to remove itself. But don't worry, in the next iteration we will still check this element.



Complexity analysis

Time complexity : O(n). Both i and nnn traverse at most n steps. In this approach, the number of assignment operations is equal to the number of elements to remove. 
So it is more efficient if elements to remove are rare.

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

        i = 0
        n = len(nums)
        
        while i < n:
            if nums[i] == val:

                # swap the current element out with the last element and dispose the last one.
                nums[i] = nums[n - 1]
                
                # reduce array size
                n = n - 1
            else:
                i = i + 1

            print(nums)

        return n



def main():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = Solution()
    print(result.removeElement(nums, val))


if __name__== "__main__" :
    main()