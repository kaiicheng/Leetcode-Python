# dict is faster than list
# if i + 1 not in dict:
# vs
# if i + 1 not in ls:

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        dict = {}

        for i in range(len(nums)):
            dict[nums[i]] = ""
        # print("dict: ", dict)

        ls = []
        for i in range(len(nums)):
            if i + 1 not in dict:
                ls.append(i + 1)
        # print("ls: ", ls)

        return ls
    
        # nums.sort()
        # ls = []
        # count = 1
        # for i in range(len(nums)):


if __name__== "__main__" :
    # nums = [4,3,2,7,8,2,3,1]
    nums = [1, 1]
    result = Solution()
    print(result.findDisappearedNumbers(nums))