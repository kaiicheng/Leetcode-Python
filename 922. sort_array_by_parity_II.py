from typing import List
from copy import copy

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        n = copy.deepcopy(nums)
        odds = []
        even = []

        for i in range(len(n)):
            if n[i] % 2 == 0:
                even.append(n[i])
                n[i] = "e"
            else:
                odds.append(n[i])
                n[i] = "o"
        
        # print("n: ", n)
        # print("odds: ", odds)
        # print("even: ", even)

        e_index = 0
        o_index = 0
        ans = []
        for i in range(len(n)):
            if i % 2 == 0:
                ans.append(even[e_index])
                e_index += 1
            else:
                ans.append(odds[o_index])
                o_index += 1
        print("ans: ", ans)

        return ans

def main(nums):
    result = Solution()
    print(result.sortArrayByParityII(nums))

if __name__== "__main__" :
    nums = [4,2,5,7]
    main(nums)
