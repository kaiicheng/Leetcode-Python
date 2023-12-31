class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        if len(s) == 1:
            return 1

        mx = 0
        l = 0
        di = {}
        di[s[0]] = 1
        # x =
        # y =
        # z =
        for r in range(1, len(s)):
            # print("l, r, s[l], s[r]: ", l, r, s[l], s[r])

            # if r == len(s) - 1:
            #     print("0!")
            #     if s[r] not in di:
            #         di[s[r]] = 1
            #     else:
            #         di[s[r]] += 1
            #     ans = sum(di.values())
            #     mx = max(mx, ans)
            if len(di) == 2 and s[r] not in di:
                # print("1!")
                # print("di: ", di)
                ans = sum(di.values())
                mx = max(mx, ans)
                # print("ans: ", ans)
                # mx = max(mx, )
                l_str = s[r - 1]
                temp_i = r - 1
                while l_str == s[temp_i]:
                    # print("l_str, temp_i, s[temp_i]: ", l_str, temp_i, s[temp_i])
                    temp_i -= 1
                    # if s[temp_i - 1] != l_str:
                    #     break
                temp_i += 1
                # print("temp_i: ", temp_i)

                l = temp_i
                # l = r - di[s[r - 1]]
                # temp = di[s[l]]
                # print("l, temp: ", l, temp)
                di = {}
                di[s[l]] = r - l
                di[s[r]] = 1
            elif s[r] not in di:
                # print("2!")
                # di = {}
                di[s[r]] = 1
                ans = sum(di.values())
                mx = max(mx, ans)
            elif s[r] in di:
                # print("3!")
                # di = {}
                # if s[r] not in di:
                #     di[s[r]] = 2
                # else:
                di[s[r]] += 1
                ans = sum(di.values())
                mx = max(mx, ans)
                # print("ans: ", ans)
            # print("di: ", di)
            # print("max: ", mx)
        return mx
    
def main(s):
    result = Solution()
    print(result.lengthOfLongestSubstringTwoDistinct(s))

if __name__== "__main__" :
    s = "ccaabbb"
    main(s)
