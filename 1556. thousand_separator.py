class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        n = str(n)
        if len(n) > 3:
            # n = n[:-3] + "." + n[-3:]
            c = 1
            for i in range(len(n) - 1, 0, -1):
                # print("i, n[i]: ", i, n[i])
                if c % 3 == 0:
                    n = n[:i] + "." + n[i:]
                # print("n: ", n)
                c += 1
        return n

def main(n):
    result = Solution()
    print(result.thousandSeparator(n))

if __name__== "__main__" :
    n = 123456789
    main(n)
