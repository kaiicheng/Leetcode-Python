class Solution:
    def maxPower(self, s: str) -> int:
        
        pre = s[0]
        cont = 1
        mx = 1
        for i in range(1, len(s)):
            if s[i] == pre:
                cont += 1
                mx = max(mx, cont)
            else:
                cont = 1
            pre = s[i]
        return mx

def main(s):
    result = Solution()
    print(result.maxPower(s))

if __name__== "__main__" :
    s = "abbcccddddeeeeedcba"
    main(s)
