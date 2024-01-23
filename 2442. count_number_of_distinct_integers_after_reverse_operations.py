from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        s = set(nums)
        for i in range(len(nums)):
            # print("i, nums[i]: ", i, nums[i])
            # print("nums: ", nums)
            cur = int(str(nums[i])[::-1])
            if cur not in s:
                s.add(cur)

        # print("s: ", s)
        return len(s)

def main(nums):
    result = Solution()
    print(result.countDistinctIntegers(nums))

if __name__== "__main__" :
    nums = [1,13,10,12,31]
    main(nums)
