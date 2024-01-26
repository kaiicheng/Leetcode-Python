class Solution:
    def sortSentence(self, s: str) -> str:
        
        s = s.split(" ")
        ls = []
        for i in range(len(s)):
            ls.append([int(s[i][-1]), s[i][:-1]])
        ls.sort()
        # print("ls: ", ls)

        ans = []
        for i in range(len(ls)):
            ans.append(ls[i][1])
        
        return " ".join(ans)

def main(s):
    result = Solution()
    print(result.sortSentence(s))

if __name__== "__main__" :
    s = "is2 sentence4 This1 a3"
    main(s)
