from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        first_level = True
        while len(nums) > 1:
            ls = []
            if first_level:
                for i in range(1, len(nums)):
                    ls.append(nums[i - 1] + nums[i])
                if len(ls) == 1:
                    ls[0] = ls[0] % 10
                first_level = False
            else:
                # temp = 0
                for i in range(1, len(nums)):
                        # print("nums[i - 1], nums[i]: ", nums[i - 1], nums[i])
                        # print("(nums[i - 1] + nums[i]) % 10: ", (nums[i - 1] + nums[i]) % 10)
                        ls.append((nums[i - 1] + nums[i]) % 10)
            # print("ls: ", ls)
            nums = ls
            # print("nums: ", nums)

        return sum(nums)

def main(nums):
    result = Solution()
    print(result.triangularSum(nums))

if __name__== "__main__" :
    nums = [1,2,3,4,5]
    main(nums)
