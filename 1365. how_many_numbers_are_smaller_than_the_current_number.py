from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        ls = []
        for i in range(len(nums)):
            c = 0
            for j in range(len(nums)):
                if i != j:
                    if nums[j] < nums[i]:
                        c += 1
            ls.append(c)
        return ls

def main(nums):
    result = Solution()
    print(result.smallerNumbersThanCurrent(nums))

if __name__== "__main__" :
    nums = [8,1,2,2,3]
    main(nums)
