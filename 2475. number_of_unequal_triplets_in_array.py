from typing import List

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        
        # brute froce

        count=0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        count += 1
                    # for d in range(k + 1, len(nums)):
                    #     if nums[a]+nums[b]+nums[c]==nums[d]:
                    #         count+=1
        return count

def main(nums):
    result = Solution()
    print(result.unequalTriplets(nums))

if __name__== "__main__" :
    nums = [4,4,2,4,3]
    main(nums)
