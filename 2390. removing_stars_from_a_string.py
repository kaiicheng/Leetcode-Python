class Solution:
    def removeStars(self, s: str) -> str:
        
        ans = []
        for i in range(len(s)):
            if s[i] != "*":
                ans.append(s[i])
            elif s[i] == "*":
                ans.pop()
        return "".join(ans)

def main(s):
    result = Solution()
    print(result.removeStars(s))

if __name__== "__main__" :
    s = "leet**cod*e"
    main(s)
