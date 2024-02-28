from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
    
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    ans += 1
        return ans

def main(nums):
    result = Solution()
    print(result.numIdenticalPairs(nums))

if __name__== "__main__" :
    nums = [1,2,3,1,1,3]
    main(nums)
