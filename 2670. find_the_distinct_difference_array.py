from typing import List
from collections import Counter

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        
        ls = []
        for i in range(1, len(nums) + 1):
            prefix = nums[:i]
            suffix = nums[i:]
            # print("prefix, suffix: ", prefix, suffix)
            c_prefix = Counter(prefix)
            c_suffix = Counter(suffix)
            ls.append(len(c_prefix) - len(c_suffix))
        return ls

def main(nums):
    result = Solution()
    print(result.distinctDifferenceArray(nums))

if __name__== "__main__" :
    nums = [1,2,3,4,5]
    main(nums)
