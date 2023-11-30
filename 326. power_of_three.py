class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        ans = -1
        while n != 1:
            
            # print("n / 3: ", n / 3)
            n = n / 3
            
            if int(n) != n:
                ans = 0
                break

        if ans == 0:
            return False
        else:
            return True

if __name__== "__main__" :
    n = 27
    # n = 45
    result = Solution()
    print(result.isPowerOfThree(n))