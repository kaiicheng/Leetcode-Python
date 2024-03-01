from collections import Counter

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        ls = list(s)
        c = Counter(s)
        one = c["1"]
        one -= 1
        zero = c["0"]
        if one == 0:
            return "0" * zero + "1"
        else:
            ans = []
            for i in range(one):
                ans.append("1")
            for i in range(zero):
                ans.append("0")
            ans.append("1")
            ans = "".join(ans)
            return ans

def main(s):
    result = Solution()
    print(result.maximumOddBinaryNumber(s))

if __name__== "__main__" :
    s = "0101"
    main(s)
