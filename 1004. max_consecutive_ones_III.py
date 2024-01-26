from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0
        for right in range(len(nums)):

            print("left, right: ", left, right)
            
            # If we included a zero in the window we reduce the value of k.
            # Since k is the maximum zeros allowed in a window.
            print("1 - nums[right]: ", 1 - nums[right])
            k -= 1 - nums[right]

            print("k: ", k)
            # A negative k denotes we have consumed all allowed flips and window has more than
            # allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1

        return right - left + 1

def main(nums, k):
    result = Solution()
    print(result.longestOnes(nums, k))

if __name__== "__main__" :
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    main(nums, k)
