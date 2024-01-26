from typing import List
import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = [[]]
        temp_ans = []
        for i in range(len(nums)):
            for j in range(len(ans)):
                # print("i, j, nums[i], ans[j]: ", i, j, nums[i], ans[j])
                # print("ans: ", ans)
                temp_ans = copy.deepcopy(ans[j])  # important! need to use daapcopy!
                temp_ans.append(nums[i])
                ans.append(temp_ans)
                # print("---end of iteration---")
            temp_ans = []
        return ans



        # ans = [[]]
        # temp_ans = []
        # for i in range(len(nums)):
        #     for j in range(len(ans)):
        #         # print("i, j, nums[i], ans[j]: ", i, j, nums[i], ans[j])
        #         # print("ans: ", ans)
        #         if ans[j] != []:
        #             temp_ans = copy.deepcopy(ans[j])
        #             temp_ans.append(nums[i])
        #         else:
        #             temp_ans = []
        #             temp_ans.append(nums[i])
            
        #         # temp_ans.append(ans[j])
        #         # temp_ans.append(nums[i])
                
        #         # print("temp_ans: ", temp_ans)
        #         ans.append(temp_ans)
        #         # print("ans: ", ans)
        #         # print("---end of iteration---")
        #     temp_ans = []
        # return ans
    
def main(nums):
    result = Solution()
    print(result.subsets(nums))

if __name__== "__main__" :
    nums = [1,2,3]
    main(nums)
