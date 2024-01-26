from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        return ans

def main(nums, target):
    result = Solution()
    print(result.targetIndices(nums, target))

if __name__== "__main__" :
    nums = [1,2,5,2,3]
    target = 2
    main(nums, target)
