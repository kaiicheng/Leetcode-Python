from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        pre = None
        for i in range(len(nums)):
            # print("i, nums[i], pre: ", i, nums[i], pre)
            if nums[i] == 1 and pre != None:
                if (i - pre) - 1 < k:
                    return False
                pre = i
            elif nums[i] == 1 and pre == None:
                pre = i
        return True



        # one pass + count

        # # initialize the counter of zeros to k to pass the first 1 in nums
        # count = k
        
        # for num in nums:
        #     # if the current integer is 1
        #     if num == 1:
        #         # check that number of zeros in-between 1s
        #         # is greater than or equal to k
        #         if count < k:
        #             return False
        #         # reinitialize counter
        #         count = 0
        #     # if the current integer is 0
        #     else:
        #         # increase the counter
        #         count += 1
                
        # return True

def main(nums, k):
    result = Solution()
    print(result.kLengthApart(nums, k))

if __name__== "__main__" :
    nums = [1,0,0,0,1,0,0,1]
    k = 2
    main(nums, k)
