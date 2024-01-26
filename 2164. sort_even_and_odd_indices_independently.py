from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        odd = []
        even = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            elif i % 2 == 1:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort()

        nums = []
        for i in range(min(len(odd), len(even))):
            nums.append(even[i])
            nums.append(odd[i])

        if len(nums) != len(even) + len(odd):
            nums.append(even[-1])
        
        return nums

def main(nums):
    result = Solution()
    print(result.sortEvenOdd(nums))

if __name__== "__main__" :
    nums = [4,1,2,3]
    main(nums)
