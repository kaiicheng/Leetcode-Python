from math import ceil
from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        # inference
        c = Counter(nums)
        ans = 0
        for i in c:
            if c[i] == 1: 
                return -1
            ans += ceil(c[i] / 3)
        return ans



        # wrong

        # c = Counter(nums)
        # print("c: ", c)

        # ans = 0
        # for i in c:
        #     # print("i, c[i]: ", i, c[i])
        #     if c[i] % 5 == 0:
        #         ans += (c[i] // 5) * 2
        #     elif c[i] % 3 == 0:
        #         ans += c[i] // 3
        #     elif c[i] % 2 == 0:
        #         ans += c[i] // 2
        #     else:
        #         return -1 
        # return ans

def main(nums):
    result = Solution()
    print(result.minOperations(nums))

if __name__== "__main__" :
    nums = [2,3,3,2,2,4,2,3,4]
    main(nums)
