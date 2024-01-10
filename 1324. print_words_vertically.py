# text.lstrip() and text.rstrip()

# text = '   Python strip   '
# left_trimmed_text = text.lstrip()
# right_trimmed_text = text.rstrip()
# print(left_trimmed_text)
# print(right_trimmed_text)

# Output:
# 'Python strip   '
# '   Python strip'

from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        s = s.split(" ")

        len_mx = 0
        for i in range(len((s))):
            len_mx = max(len_mx, len(s[i]))
        # print("len_mx: ", len_mx)

        ans = [[] for i in range(len_mx)]
        # print("ans: ", ans)

        for i in range(len(s)):
            # print("i, s[i]: ", i, s[i])
            for j in range(len_mx):
                if j < len(s[i]):
                    # print("j, s[i][j]: ", j, s[i][j])
                    ans[j] += s[i][j]
                else:
                    # print("empty!")
                    ans[j] += " "
        # print("ans: ", ans)

        res = []
        for i in ans:
            temp = ""
            for j in i:
                # print("i, j: ", i ,j)
                temp += j
            temp = temp.rstrip()
            res.append(temp)
        # print("res: ", res)

        return res

def main(s):
    result = Solution()
    print(result.printVertically(s))

if __name__== "__main__" :
    s = "CONTEST IS COMING"
    main(s)
