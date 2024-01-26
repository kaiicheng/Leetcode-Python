from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        ans = []

        for i in range(len(nums)):
            ans.insert(index[i], nums[i])
        return ans

def main(nums, index):
    result = Solution()
    print(result.createTargetArray(nums, index))

if __name__== "__main__" :
    nums = [0,1,2,3,4]
    index = [0,1,2,2,1]
    main(nums, index)
