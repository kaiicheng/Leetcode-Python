class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        s = s.split(" ")
        ans = s[:k]
        return " ".join(ans)

def main(s, k):
    result = Solution()
    print(result.truncateSentence(s, k))

if __name__== "__main__" :
    s = "Hello how are you Contestant"
    k = 4
    main(s, k)
