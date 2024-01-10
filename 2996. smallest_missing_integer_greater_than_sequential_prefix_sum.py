# prefix is a contiguous subArray starting at index 0

from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        count = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += nums[i]
            else:
                break

        while True:
            if count not in nums:
                return count
            else:
                count+=1
            
    
        # wrong

        # seq = [[nums[0]]]
        # pre = nums[0]
        
        # l = 0
        # temp = [nums[0]]
        # for r in range(1, len(nums)):
        #     # print("pre: ", pre)
        #     # print("l, nums[l]: ", l, nums[l])
        #     # print("r, nums[r]: ", r, nums[r])
        #     if nums[r] == pre + 1:
        #         temp.append(nums[r])
        #     else:
        #         seq.append(temp)
        #         temp = []
        #         l = r
        #     pre = nums[r]
        #     l += 1

        #     seq.append(temp)

        #     # print("temp, seq: ", temp, seq)
        #     # print("---end of iteration---")
        
        # mx = float("-inf")
        # for i in range(len(seq)):
        #     mx = max(mx, sum(seq[i]))
        # # print("mx: ", mx)
        
        # while mx in nums:
        #     mx += 1
        #     if mx not in nums:
        #         break

        # return mx

def main(nums):
    result = Solution()
    print(result.missingInteger(nums))

if __name__== "__main__" :
    nums = [3,4,5,1,12,14,13]
    main(nums)