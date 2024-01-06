from typing import List

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            # % => mod
            if i % 10 == nums[i]:
                return i
        return -1

def main(nums):
    result = Solution()
    print(result.smallestEqual(nums))

if __name__== "__main__" :
    nums = [4,3,2,1]
    main(nums)
