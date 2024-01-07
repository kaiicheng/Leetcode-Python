from collections import defaultdict
from typing import List

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:

        # using itertools.combinations
        # return sum(1  for a,b,c,d in itertools.combinations(nums, 4) if a+b+c == d)



        # brute froce

        # count=0
        # for a in range(len(nums)):
        #     for b in range(a+1,len(nums)):
        #         for c in range(b+1,len(nums)):
        #             for d in range(c+1,len(nums)):
        #                 if nums[a]+nums[b]+nums[c]==nums[d]:
        #                     count+=1
        # return count



        # prefix sum
        count = 0
        tot2 = defaultdict(int)

        for c in range(2, len(nums)-1):
            # print("c: ", c)
            b = c-1
            # a and b part - prefix sum.
            for a in range(b):
                tot2[nums[a]+nums[b]] += 1
                # print("tot2: ", tot2)

            # c and d part - nums[d]-nums[c] == nums[a]+nums[b].
            for d in range(c+1, len(nums)):
                count += tot2[nums[d]-nums[c]]
                # print("tot2: ", tot2)

            # print("tot2: ", tot2)
        return count

def main(nums):
    result = Solution()
    print(result.countQuadruplets(nums))

if __name__== "__main__" :
    nums = [3,3,6,4,5]
    main(nums)
