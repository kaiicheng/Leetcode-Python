from typing import List
from collections import Counter

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        c = Counter(nums)
        # print("c: ", c)

        ans = []
        for i in c:
            if c[i] == 1 and i - 1 not in c and i + 1 not in c:
                ans.append(i)

        return ans

def main(nums):
    result = Solution()
    print(result.findLonely(nums))

if __name__== "__main__" :
    nums = [10,6,5,8]
    main(nums)
