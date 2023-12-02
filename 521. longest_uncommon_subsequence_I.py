class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        ans = max(len(a), len(b))
        return ans

def main(a, b):
    result = Solution()
    print(result.findLUSlength(a, b))

if __name__== "__main__" :
    a = "aba"
    b = "cdc"
    main(a, b)
