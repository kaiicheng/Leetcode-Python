from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if i == 0:
                l = []
                r = nums[1:]
            elif i == len(nums) - 1:
                l = nums[:len(nums) - 1]
                r = []
            else:
                l = nums[:i]
                r = nums[i + 1:]
            # print("l, r: ", l, r)
            if sum(l) == sum(r):
                return i
        return -1

def main(nums):
    result = Solution()
    print(result.findMiddleIndex(nums))

if __name__== "__main__" :
    nums = [2,3,-1,8,4]
    main(nums)
