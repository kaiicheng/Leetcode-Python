class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        st = str(n)
        prod = int(st[0])
        total = int(st[0])
        for i in range(1, len(st)):
            prod *= int(st[i])
            total += int(st[i])
        return prod - total
    
def main(n):
    result = Solution()
    print(result.subtractProductAndSum(n))

if __name__== "__main__" :
    n = 234
    main(n)
