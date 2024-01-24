from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maximus = 0
        cont = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cont += 1
                maximus = max(cont, maximus)
            # if cont > 0 and nums[i] == 1:
            #     cont += 1
            else:
                cont = 0

        return maximus 

def main(nums):
    result = Solution()
    print(result.findMaxConsecutiveOnes(nums))

if __name__== "__main__" :
    nums = [1,1,0,1,1,1]
    main(nums)
