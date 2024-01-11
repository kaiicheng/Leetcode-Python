class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        ls = []
        for i in range(len(s)):
            if s[i] not in ls:
                ls.append(s[i])
            else:
                return s[i]

def main(s):
    result = Solution()
    print(result.repeatedCharacter(s))

if __name__== "__main__" :
    s = "abccbaacz"
    main(s)
