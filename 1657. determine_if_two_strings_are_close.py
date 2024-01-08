# if any 2 strings are close, they always satisfy follow conditions:
# 1: Every character that exists in word1 must exist in word2 as well, irrespective of the frequency.
# 2: The frequency of all the characters is always the same. In the above example for string uua

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1Map = Counter(word1)
        word2Map = Counter(word2)
        # print("word1Map, word2Map: ", word1Map, word2Map)

        # Getting keys and frequency lists
        word1KeySet = sorted(list(word1Map.keys()))
        word2KeySet = sorted(list(word2Map.keys()))
        # print("word1KeySet, word2KeySet: ", word1KeySet, word2KeySet)

        word1FrequencyList = sorted(list(word1Map.values()))
        word2FrequencyList = sorted(list(word2Map.values()))
        # print("word1FrequencyList, word2FrequencyList: ", word1FrequencyList, word2FrequencyList)

        return word1KeySet == word2KeySet and word1FrequencyList == word2FrequencyList

def main(word1, word2):
    result = Solution()
    print(result.closeStrings(word1, word2))

if __name__== "__main__" :
    word1 = "cabbba"
    word2 = "abbccc"
    main(word1, word2)
