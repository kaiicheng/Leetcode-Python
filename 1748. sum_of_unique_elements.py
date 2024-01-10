from typing import List
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        ans = 0
        for i in c:
            if c[i] == 1:
                ans += i
        return ans

def main(nums):
    result = Solution()
    print(result.expand(nums))

if __name__== "__main__" :
    nums = [1,2,3,4,5]
    main(nums)
