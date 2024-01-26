from collections import List

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        ans = 0
        for i in range(len(nums[0])):
            cur = []
            for j in range(len(nums)):
                # print("j, nums[j]: ", j, nums[j])
                cur.append(max(nums[j]))
                nums[j].remove(max(nums[j]))
                # print("nums[j]: ", nums[j])
            temp = max(cur)
            ans += temp
        return ans

def main(nums):
    result = Solution()
    print(result.matrixSum(nums))

if __name__== "__main__" :
    nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
    main(nums)
