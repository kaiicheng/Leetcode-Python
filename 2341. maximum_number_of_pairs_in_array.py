from typing import List
from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        # cur_nums = copy.deepcopy(nums)

        # for i in range(len(nums)):
        #     if nums[i] in cur_nums 

        c = Counter(nums)
        # print("c: ", c)
        ans = 0
        rest = 0
        for i in c:
            # print("i: ", i)
            if c[i] % 2 == 0:
                ans += c[i] // 2
            else:
                ans += c[i] // 2
                rest += 1
        
        return [ans, rest]

def main(nums):
    result = Solution()
    print(result.numberOfPairs(nums))

if __name__== "__main__" :
    nums = [1,3,2,1,3,2,2]
    main(nums)
