from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        while original in nums:
            original *= 2
        return original

def main(nums, original):
    result = Solution()
    print(result.findFinalValue(nums, original))

if __name__== "__main__" :
    nums = [5,3,6,1,12]
    original = 3
    main(nums, original)
