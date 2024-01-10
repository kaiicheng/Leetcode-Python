class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        if n % 2 == 0:
            return n
        else:
            return n * 2

def main(n):
    result = Solution()
    print(result.smallestEvenMultiple(n))

if __name__== "__main__" :
    n = 7
    main(n)