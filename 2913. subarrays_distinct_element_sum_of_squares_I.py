from typing import List
from collections import Counter

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        ans = 0
        l = 0
        while l < len(nums):
            for r in range(1, len(nums) + 1):
                if l < r:
                    # print("l, r: ", l, r)
                    temp_s = nums[l:r]
                    # print("temp_s: ", temp_s)
                    c = Counter(temp_s)
                    # print("c: ", c)
                    ans += len(c) ** 2
                    # print("ans: ", ans)
            l += 1
        return ans
    
def main(nums):
    result = Solution()
    print(result.sumCounts(nums))

if __name__== "__main__" :
    nums = [1,2,1]
    main(nums)
