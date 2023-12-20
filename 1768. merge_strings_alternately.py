class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ans = []
        n = min(len(word1), len(word2))
        for i in range(n):
            ans.append(word1[i])
            ans.append(word2[i])

        if len(word1) == len(word2):
            pass
        if len(word1) > len(word2):
            for i in range(max(len(word1), len(word2)) - len(word2)):
                ans.append(word1[i + n])
        if len(word1) < len(word2):
            for i in range(max(len(word1), len(word2)) - len(word1)):
                ans.append(word2[i + n])
        return "".join(ans)
    
def main(word1, word2):
    result = Solution()
    print(result.mergeAlternately(word1, word2))

if __name__== "__main__" :
    word1 = "ab"
    word2 = "pqrs"
    main(word1, word2)
