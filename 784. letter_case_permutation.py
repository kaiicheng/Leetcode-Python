from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        # recursion
        # ans = [[]]

        # for char in S:
        #     n = len(ans)
        #     if char.isalpha():
        #         for i in xrange(n):
        #             ans.append(ans[i][:])
        #             ans[i].append(char.lower())
        #             ans[n+i].append(char.upper())
        #     else:
        #         for i in xrange(n):
        #             ans[i].append(char)

        # return map("".join, ans)



        # brute force

        ans = [s]

        for i in range(len(s)):
            if s[i].isalpha():
                
                if len(ans) != 1:
                    # uppercase
                    for j in range(len(ans)):
                        u = ans[j][:i] + ans[j][i].upper() + ans[j][i + 1:]
                        if u not in ans:
                            ans.append(u)
                    # lowercase
                    for j in range(len(ans)):
                        l = ans[j][:i] + ans[j][i].lower() + ans[j][i + 1:]
                        if l not in ans:
                            ans.append(l)
                else:
                    u = s[:i] + s[i].upper() + s[i + 1:]
                    if u not in ans:
                        ans.append(u)
                    l = s[:i] + s[i].lower() + s[i + 1:]
                    if l not in ans:
                        ans.append(l)
                # print("ans: ", ans)
        return ans

def main(s):
    result = Solution()
    print(result.letterCasePermutation(s))

if __name__== "__main__" :
    s = "a1b2"
    main(s)
