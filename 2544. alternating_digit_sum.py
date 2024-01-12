class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        n = str(n)
        ans = 0
        ans += int(n[0])
        neg = -1
        for i in range(1, len(n)):
            ans += int(n[i]) * neg
            neg *= -1
        return ans
    
def main(n):
    result = Solution()
    print(result.alternateDigitSum(n))

if __name__== "__main__" :
    n = 886996
    main(n)