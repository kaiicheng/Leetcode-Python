from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos = []
        neg = []
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            elif nums[i] > 0:
                pos.append(nums[i])

        nums = []
        for i in range(len(pos)):
            nums.append(pos[i])
            nums.append(neg[i])
        
        return nums

def main(nums):
    result = Solution()
    print(result.rearrangeArray(nums))

if __name__== "__main__" :
    nums = [3,1,-2,-5,2,-4]
    main(nums)
