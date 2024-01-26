from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        nums.sort()
        print("nums: ", nums)
        dict = {}
        repeat = -1
        for i in range(len(nums)):
            # print("nums[i]: ", nums[i])
            # print("nums[i] not in dict: ", nums[i] not in dict)
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                repeat = nums[i]

        nums.remove(repeat)
        # nums.sort()
        print("nums: ", nums)

        missing = -1
        for i in range(len(nums)):
            print("i + 1: ", i + 1)
            print("nums[i]: ", nums[i])
            if nums[i] != i + 1:
                missing = i +1
                break
        if len(nums) == 1:
            if nums[0] == 1:
                missing = 2
            else:
                missing = 1
        if missing == -1:
            missing = len(nums) + 1
        # if missing == -1:
        #     missing = len(nums)
        print("missing: ", missing)

        return [repeat, missing]

def main(nums):
    result = Solution()
    print(result.findErrorNums(nums))

if __name__== "__main__" :
    nums = [1,2,2,4]
    main(nums)