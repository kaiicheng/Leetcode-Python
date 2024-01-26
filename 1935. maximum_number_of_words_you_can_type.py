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
