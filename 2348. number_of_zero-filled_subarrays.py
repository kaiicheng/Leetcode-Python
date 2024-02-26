from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        ans, num_subarray = 0, 0
        
        # Iterate over nums, if num = 0, it has 1 more zero-filled subarray
        # than the previous one, otherwise, it has 0 zero-filled subarray.
        for num in nums:
            # print("num: ", num)
            # print("num_subarray: ", num_subarray)
            if num == 0: 
                num_subarray += 1
            else: 
                num_subarray = 0
            ans += num_subarray
            
        return ans
    


        # wrong

        # l = 0
        # zero = []
        # for r in range(l + 1, len(nums)):
        #     print("l, r: ", l, r)
        #     if r == len(nums) - 1 and nums[r] == 0:
        #         zero.append(nums[l: r + 1])
        #     elif nums[l] == 0 and nums[r] == 0:
        #         pass
        #     elif nums[l] == 0 and nums[r] != 0:
        #         zero.append(nums[l: r])
        #         l = r
        #     elif nums[l] != 0 and nums[r] == 0:
        #         l = r
        #     elif nums[l] != 0 and nums[r] != 0:
        #         pass

        #     print("zero: ", zero)
        
        # ans = 0
        # for i in range(len(zero)):
        #     # for j in range(len(zero[i])):
        #     ans += len()

        # return -1

def main(nums):
    result = Solution()
    print(result.zeroFilledSubarray(nums))

if __name__== "__main__" :
    nums = [1,3,0,0,2,0,0,4]
    main(nums)
