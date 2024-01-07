from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        ls = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] % 3 == 0:
                ls.append(nums[i])
        # print("ls: ", ls)

        if len(ls) == 0:
            return 0
        else:
            return (sum(ls) // len(ls))

def main(nums):
    result = Solution()
    print(result.averageValue(nums))

if __name__== "__main__" :
    nums = [1,3,6,10,12,15]
    main(nums)
