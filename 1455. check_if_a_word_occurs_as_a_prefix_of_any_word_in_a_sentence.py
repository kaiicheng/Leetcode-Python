class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sentence = sentence.split(" ")
        # print("sentence: ", sentence)

        for i in range(len(sentence)):
            # print("i, sentence[i]: ", i, sentence[i])
            # print("sentence[i][:len(searchWord)]: ", sentence[i][:len(searchWord)])
            if searchWord == sentence[i][:len(searchWord)]:
                return i + 1
        return -1

def main(sentence, searchWord):
    result = Solution()
    print(result.isPrefixOfWord(sentence, searchWord))

if __name__== "__main__" :
    sentence = "i love eating burger"
    searchWord = "burg"
    main(sentence, searchWord)
