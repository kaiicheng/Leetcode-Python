from typing import List

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        val = 0
        if len(nums) == 1:
            val += int(nums[0]) 
        else:
            while len(nums) > 0:
                if len(nums) == 1:
                    val += int(nums[0])
                    break
                # print("nums: ", nums)
                # print("val: ", val)
                first = nums[0]
                last = nums[-1]
                val += int(str(first) + str(last))
                nums = nums[1:-1]
        return val
    
def main(nums):
    result = Solution()
    print(result.expafindTheArrayConcValnd(nums))

if __name__== "__main__" :
    nums = [7,52,2,4]
    main(nums)
