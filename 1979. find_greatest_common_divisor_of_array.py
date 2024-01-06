from math import gcd
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        mx = max(nums)
        mi = min(nums)
        return gcd(mx, mi)



        # Euclidean algorithm

        # min = max = nums[0]
        # for i in nums:
        #     if i < min:
        #         min = i
        #     if i > max:
        #         max = i

        # while max and min:
        #     if max > min:
        #         max %= min
        #     else:
        #         min %= max
        # return max if max > min else min

def main(nums):
    result = Solution()
    print(result.findGCD(nums))

if __name__== "__main__" :
    nums = [7,5,6,8,3]
    main(nums)
