from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # hash table

        c = Counter(nums)
        # print("c: ", c)
        ans = [i for i in c if c[i] == 1]
        # print("ans: ", ans)
        return ans[0]

def main(nums):
    result = Solution()
    print(result.singleNumber(nums))

if __name__== "__main__" :
    nums = [0,1,0,1,0,1,99]
    main(nums)
