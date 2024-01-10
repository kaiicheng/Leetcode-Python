class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        m = 0
        while n > 1:
            # print("n, m: ", n, m)
            if n % 2 == 0:
                m += n // 2        
                n = n // 2
            elif n % 2 == 1:
                m += (n - 1) // 2
                n = ((n - 1) // 2) + 1
        return m
    
def main(n):
    result = Solution()
    print(result.numberOfMatches(n))

if __name__== "__main__" :
    n = 14
    main(n)
