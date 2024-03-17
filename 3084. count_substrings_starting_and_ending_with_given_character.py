class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
  
        ans = 0
        freq = s.count(c)
        # print("freq: ", freq)
        
        while freq > 0:
            ans += freq
            freq -= 1
        # ans += freq
        # ans += freq * 2
        return ans

        # Time Limit Exceed

        # brute force
        # ans = 0
        
        # l = 0
        # while l < len(s):
        #     for r in range(l, len(s)):
        #         # print("l, r: ", l, r)
        #         cur = s[l:r + 1]
        #         # print("cur: ", cur)
        #         if cur[0] == c and cur[-1] == c:
        #             ans += 1
        #     l += 1
        
        # return ans
    
def main(s, c):
    result = Solution()
    print(result.countSubstrings(s, c))

if __name__== "__main__" :
    s = "abada"
    c = "a"
    main(s, c)
