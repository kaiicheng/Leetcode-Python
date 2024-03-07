class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n == 0:
            return 0

        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1

        for i in range(n):
            # if i == 0 or i == 1:
            #     pass
            if 2 <= 2 * i and 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 <= 2 * i + 1 and 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] +  nums[i + 1]
        # print("nums: ", nums)

        return max(nums)

def main(n):
    result = Solution()
    print(result.getMaximumGenerated(n))

if __name__== "__main__" :
    n = 7
    main(n)
