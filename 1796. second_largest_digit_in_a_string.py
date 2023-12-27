# .isdigit()
# .isnumeric()

class Solution:
    def secondHighest(self, s: str) -> int:
        
        digit = {}
        for i in range(len(s)):
            if s[i].isnumeric() and s[i] not in digit:
                digit[int(s[i])] = ""
        # print("digit: ", digit)

        ls = list(digit)
        ls.sort()
        # print("ls: ", ls)

        if len(ls) < 2:
            return -1
        else:
            return ls[-2]

def main(s):
    result = Solution()
    print(result.secondHighest(s))

if __name__== "__main__" :
    s = "dfa12321afd"
    main(s)

