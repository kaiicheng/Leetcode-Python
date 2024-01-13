# can use set to get overlapping elements directly

# s = "leetcode"
# t = "coats"

# c_s:  Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})
# c_t:  Counter({'c': 1, 'o': 1, 'a': 1, 't': 1, 's': 1})
# c_s - c_t:  Counter({'e': 3, 'l': 1, 'd': 1})
# c_t - c_s:  Counter({'a': 1, 's': 1})

from typing import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        # s = "cotxazilut"
        # t = "nahrrmcchxwrieqqdwdpneitkxgnt"

        c_s = Counter(s)
        c_t = Counter(t)
        print("c_s: ", c_s)
        print("c_t: ", c_t)
        print("c_s - c_t: ", c_s - c_t)
        print("c_t - c_s: ", c_t - c_s)

        ans = 0
        gap = c_s - c_t + (c_t - c_s)
        # print("gap: ", gap)
        for i in gap.values():
            ans+=i
        return ans



        # c_s = Counter(s)
        # c_t = Counter(t)
        # # print("c_s: ", c_s)
        # # print("c_t: ", c_t)

        # s_lack = []
        # t_lack = []

        # for i in c_s:
        #     if i not in c_t:
        #         for j in range(c_s[i]): 
        #             t_lack.append(i)
        #     elif i in c_t and c_t[i] != c_s[i]:
        #         # print("i, c_t[i], c_s[i]: ", i, c_t[i], c_s[i])
        #         for j in range(abs(c_t[i] - c_s[i])):
        #             t_lack.append(i)

        # for i in c_t:
        #     if i not in c_s:
        #         for j in range(c_t[i]):
        #             s_lack.append(i)
        #     # elif i in c_s and c_t[i] != c_s[i]:
        #     #     print("i, c_t[i], c_s[i]: ", i, c_t[i], c_s[i])
        #     #     for j in range(abs(c_t[i] - c_s[i])):
        #     #         s_lack.append(i)

        # # print("s_lack, t_lack: ", s_lack, t_lack)

        # return len(s_lack) + len(t_lack)

def main(s, t):
    result = Solution()
    print(result.minSteps(s, t))

if __name__== "__main__" :
    s = "cotxazilut"
    t = "nahrrmcchxwrieqqdwdpneitkxgnt"
    main(s, t)
