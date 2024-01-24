from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        c = Counter(nums)
        for i in c:
            if c[i] % 2 != 0:
                return False
        return True

def main(nums):
    result = Solution()
    print(result.divideArray(nums))

if __name__== "__main__" :
    nums = [3,2,3,2,2,2]
    main(nums)
