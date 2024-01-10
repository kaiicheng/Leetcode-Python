from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        return nums + nums

def main(nums):
    result = Solution()
    print(result.getConcatenation(nums))

if __name__== "__main__" :
    nums = [1,3,2,1]
    main(nums)
