class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        if word.find(ch) == -1:
            return word
        else:
            i = word.find(ch)
            temp = word[:i + 1]
            temp = temp[::-1]
            temp = temp + word[i + 1:]
        return temp

def main(word, ch):
    result = Solution()
    print(result.reversePrefix(word, ch))

if __name__== "__main__" :
    word = "abcdefd"
    ch = "d"
    main(word, ch)
