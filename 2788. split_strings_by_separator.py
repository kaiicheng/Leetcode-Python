from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        
        ls = []
        for i in range(len(words)):
            temp = words[i].split(separator)
            for j in range(len(temp)):
                if temp[j] is not "":
                    ls.append(temp[j])
        
        # print("ls: ", ls)
        return ls

def main(words, separator):
    result = Solution()
    print(result.splitWordsBySeparator(words, separator))

if __name__== "__main__" :
    words = ["one.two.three","four.five","six"]
    separator = "."
    main(words, separator)
