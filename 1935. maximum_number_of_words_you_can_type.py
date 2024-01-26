class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        text = text.split(" ")
        wrong = 0
        for i in range(len(text)):
            for j in brokenLetters:
                if j in text[i]:
                    wrong += 1
                    break
        return len(text) - wrong

def main(text, brokenLetters):
    result = Solution()
    print(result.canBeTypedWords(text, brokenLetters))

if __name__== "__main__" :
    text = "hello world"
    brokenLetters = "ad"
    main(text, brokenLetters)
