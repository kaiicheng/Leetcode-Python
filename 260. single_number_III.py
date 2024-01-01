from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        c = Counter(nums)
        return [i for i in c if c[i] == 1]

def main(nums):
    result = Solution()
    print(result.singleNumber(nums))

if __name__== "__main__" :
    nums = [1,2,1,3,2,5]
    main(nums)
