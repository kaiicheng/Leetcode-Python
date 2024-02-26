from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        start = 1
        while start:
            all_pos = True
            cur = start
            for i in range(len(nums)):
                # print("---iteration start---")
                # print("i, nums[i]: ", i, nums[i])
                # print("cur: ", cur)
                if cur + nums[i] < 1:
                    all_pos = False
                    start += 1
                    break
                else:
                    cur += nums[i]
                # print("cur: ", cur)
                # print("start: ", start)

            if all_pos:
                return start

        return start

def main(nums):
    result = Solution()
    print(result.minStartValue(nums))

if __name__== "__main__" :
    nums = [-3,2,-3,4,2]
    main(nums)
