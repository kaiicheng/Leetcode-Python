class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        vowel = "aeiouAEIOU"

        a = s[: len(s)// 2]
        b = s[len(s)// 2 :]
        # print("a, b: ", a, b)

        count_a = 0
        count_b = 0
        for i in range(len(a)):
            if a[i] in vowel:
                count_a +=1
            if b[i] in vowel:
                count_b +=1

        return True if count_a == count_b else False

def main(s):
    result = Solution()
    print(result.halvesAreAlike(s))

if __name__== "__main__" :
    s = "textbook"
    main(s)
