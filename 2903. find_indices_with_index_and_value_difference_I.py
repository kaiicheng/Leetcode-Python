from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        
        n = len(nums)
        ans = None
        for i in range(n):
            for j in range(n):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    ans = [i, j]
        if ans is None:
            return [-1, -1]
        else:
            return ans
        
def main(nums, indexDifference, valueDifference):
    result = Solution()
    print(result.findIndices(nums, indexDifference, valueDifference))

if __name__== "__main__" :
    nums = [5,1,4,1]
    indexDifference = 2
    valueDifference = 4
    main(nums, indexDifference, valueDifference)
