from typing import List
import copy

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # [1, 4] and [4, 1] are same. To avoid this, need to sort first!
        nums.sort()

        ans = [[]]
        temp_ans = []
        for i in range(len(nums)):
            for j in range(len(ans)):
                # print("i, j, nums[i], ans[j]: ", i, j, nums[i], ans[j])
                # print("ans: ", ans)
                temp_ans = copy.deepcopy(ans[j])  # important! need to use daapcopy!
                temp_ans.append(nums[i])
                if temp_ans not in ans:
                    ans.append(temp_ans)
                # print("---end of iteration---")
            temp_ans = []
        return ans

def main(nums):
    result = Solution()
    print(result.subsetsWithDup(nums))

if __name__== "__main__" :
    nums = [1,2,2]
    main(nums)
