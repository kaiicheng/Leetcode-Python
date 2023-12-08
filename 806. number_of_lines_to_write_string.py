from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        # print("odr(a): ", ord("a"))  # 97
        # print("odr(b): ", ord("b"))  # 98

        ans = []
        line = 0
        cur_str = []
        cur_total = 0
        for i in range(len(s)):
          # print("s[i]", s[i])
          # print("cur_total: ", cur_total)
          # print("cur_str: ", cur_str)
          if cur_total + widths[ord(s[i]) - 97] > 100:
            line += 1
            cur_str.append("Next Line!")
            cur_total = widths[ord(s[i]) - 97]
          elif cur_total + widths[ord(s[i]) - 97] == 100:
            line += 1
            cur_str.append(s[i])
            cur_str.append("Next Line!")
            cur_total = 0
          else:
            cur_str.append(s[i])
            cur_total += widths[ord(s[i]) - 97]
        # print("line, cur_total: ", line, cur_total)

        if cur_total == 0:
          line -= 1
          cur_total = 100
        if len(cur_str) > 0:
          line += 1

        print("line, cur_total: ", line, cur_total)

        return line, cur_total

def main(widths, s):
    result = Solution()
    print(result.numberOfLines(widths, s))

if __name__== "__main__" :
    widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    s = "abcdefghijklmnopqrstuvwxyz"
    main(widths, s)
