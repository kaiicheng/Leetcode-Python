from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        print("c: ", c)
        ls = list(c.values())
        # print("ls: ", ls)
        mx = max(ls)
        # print("mx: ", mx)

        ans = 0
        for i in c:
            # print("i, c[i]: ", i, c[i])
            if c[i] == mx:
                ans += c[i]
        
        return ans

def main(nums):
    result = Solution()
    print(result.maxFrequencyElements(nums))

if __name__== "__main__" :
    nums = [1,2,2,3,1,4]
    main(nums)
