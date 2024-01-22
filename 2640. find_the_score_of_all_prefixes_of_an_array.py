from typing import List

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        
        ls = []
        ans = []
        mx = float("-inf")
        for i in range(len(nums)):
            # print("i, nums[i]: ", i, nums[i])
            if i == 0:
                mx = nums[i]

            ls.append(nums[i])

            if nums[i] > mx:        
                mx = nums[i]
            ans.append(nums[i] + mx)
            # print("ls: ", ls)
            # print("ans: ", ans)
        
        result = [ans[0]]
        pre = ans[0]
        for i in range(1, len(ans)):
            result.append(pre + ans[i])
            pre = result[i]
        return result

def main(nums):
    result = Solution()
    print(result.findPrefixScore(nums))

if __name__== "__main__" :
    nums = [1,1,2,4,8,16]
    main(nums)
