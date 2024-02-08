class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        alpha = "abcdefghijklmnopqrstuvwxyz"
        di = {}
        count = 1
        for i in alpha:
            di[i] = count
            count += 1
        # print("di: ", di)

        if len(s) == 1:
            return 1

        l = 0
        mx = 0
        while l < len(s):
            temp = 1
            for r in range(l, len(s)):
                if l < r:
                    # print("l, r: ", l, r)
                    # print("s[l:r]: ", s[l:r + 1])
                    # print("temp: ", temp)
                    
                    # print("ord(s[l]), ord(s[r]): ", ord(s[l]), ord(s[r]))
                    # print("temp: ", temp)
                    # print((di[s[r]] - di[s[l]]))
                    
                    if ord(s[l]) + temp == ord(s[r]):
                        mx = max(mx, r - l + 1)
                        temp += 1
                    else:
                        # l += 1
                        temp = 1
                        break
                    # print("mx: ", mx)
                    # print("---end of iteration---")
            l += 1

        if mx == 0:
            return 1
        else:
            return mx



        # Time Limit Exceeded

        # alpha = "abcdefghijklmnopqrstuvwxyz"

        # if len(s) == 1:
        #     return 1

        # l = 0
        # mx = 0
        # while l < len(s):
        #     # temp = 1
        #     for r in range(l + 1, len(s)):

        #         # print("l, r: ", l, r)
        #         # print("s[l:r]: ", s[l:r + 1])
                
        #         cur = s[l:r + 1]
        #         if cur in alpha:
        #             mx = max(mx, len(cur))

        #     l += 1

        # if mx == 0:
        #     return 1
        # else:
        #     return mx

def main(s):
    result = Solution()
    print(result.longestContinuousSubstring(s))

if __name__== "__main__" :
    s = "abacaba"
    main(s)
