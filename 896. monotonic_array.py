from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        pre = nums[0]
        inc = False
        dec = False
        for i in range(1, len(nums)):
            if nums[i] != pre:
                if pre < nums[i]:
                    inc = True
                elif pre > nums[i]:
                    dec = True
                break
        # print("inc, dec: ", inc, dec)

        for i in range(1, len(nums)):
            # print("i: ", i)
            if inc:
                if pre <= nums[i]:
                    pre = nums[i]
                else:
                    return False
            elif dec:
                if pre >= nums[i]:
                    pre = nums[i]
                else:
                    return False
        return True



        # wrong

        # pre = nums[0]
        
        # inc = True
        # for i in range(1, len(nums)):
        #     if pre <= nums[i]:
        #         pass
        #     else:
        #         inc = False
        #         break
        
        # pre = nums[0]
        
        # dec = True
        # for i in range(1, len(nums)):
        #     if pre >= nums[i]:
        #         pass
        #     else:
        #         dec = False
        #         break
        # print("inc, dec: ", inc, dec)

        # if inc and not dec:
        #     return True
        # elif dec and not inc:
        #     return True
        # else:
        #     return False

def main(nums):
    result = Solution()
    print(result.isMonotonic(nums))

if __name__== "__main__" :
    nums = [1,3,2]
    main(nums)
