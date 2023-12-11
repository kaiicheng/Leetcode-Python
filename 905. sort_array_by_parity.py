from typing import List
from copy import copy

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        n = copy.deepcopy(nums)
        ans = []

        for i in range(len(n)):
            if n[i] % 2 == 0:
                ans.append(n[i])
                n[i] = ""
        
        for i in range(len(n)):
            if n[i] != "":
                ans.append(n[i])
        print("ans: ", ans)
            
        return ans

def main(nums):
    result = Solution()
    print(result.sortArrayByParity(nums))

if __name__== "__main__" :
    nums = [3,1,2,4]
    main(nums)
