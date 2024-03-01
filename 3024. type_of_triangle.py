from typing import List
from collections import Counter

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        nums.sort()
        print("nums: ", nums)
        if nums[0] + nums[1] > nums[2]:
            c = Counter(nums)
            if len(c) == 1:
                return "equilateral"
            elif len(c) == 2:
                return "isosceles"
            elif len(c) == 3:
                return "scalene"

        else:
            return "none"

def main(nums):
    result = Solution()
    print(result.triangleType(nums))

if __name__== "__main__" :
    nums = [1,2,3,4]
    main(nums)
