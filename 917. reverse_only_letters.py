# .isalpha()
# .isdigit()

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        ls = [i for i in s]
        # print("ls: ", ls)

        l = 0
        r = len(ls) - 1
        while l <= r:
            if ls[l].isalpha() and ls[r].isalpha():
                temp = ls[r]
                ls[r] = ls[l]
                ls[l] = temp
                l += 1
                r -= 1
            elif ls[l].isalpha() is False and ls[r].isalpha() is False:
                l += 1
                r -= 1
            elif ls[l].isalpha() is False and ls[r].isalpha() is True:
                l += 1
            elif ls[l].isalpha() is True and ls[r].isalpha() is False:
                r -= 1
        return "".join(ls)



        # stack

        # letters = [c for c in s if c.isalpha()]
        # print("letters: ", letters)
        # ans = []

        # for c in s:
        #     if c.isalpha():
        #         ans.append(letters.pop())
        #     else:
        #         ans.append(c)
        #     print("ans: ", ans)
        # return "".join(ans)

def main(s):
    result = Solution()
    print(result.reverseOnlyLetters(s))

if __name__== "__main__" :
    s = "Test1ng-Leet=code-Q!"
    main(s)
