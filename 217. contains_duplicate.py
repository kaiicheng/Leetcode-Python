from typing import List

# the run time of list (for i in list) is O(N), so Time Limit Exceeded
# so use dictionary (hashmap).
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # visited_num = []
        visited_num = {}
        for i in range(len(nums)):
            if nums[i] in visited_num:
                return True
            else:
                visited_num[nums[i]] = ""
        return False

if __name__== "__main__" :
    nums = [1,2,3,1]
    result = Solution()
    print(result.containsDuplicate(nums))
