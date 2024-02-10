class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ans = []

        l = 0
        while l < len(s):
            for r in range(l, len(s) + 1):
                if l < r:
                    # print("l, r: ", l, r)
                    cur = s[l:r]
                    # print("cur: ", cur)
                    if cur[::-1] == s[l:r]:
                        ans.append(s[l:r])
            l += 1
        
        return len(ans)

def main(s):
    result = Solution()
    print(result.countSubstrings(s))

if __name__== "__main__" :
    s = "aaa"
    main(s)
