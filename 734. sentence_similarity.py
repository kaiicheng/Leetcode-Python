# defaultdict usage

# dictionary cannot handle KeyError case, if key not in the dictionary
# KeyError: 'painting'

from collections import defaultdict
from typing import List

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        if len(sentence1) != len(sentence2):
            return False
        wordToSimilarWords = defaultdict(set)
        print(defaultdict)
        # print("wordToSimilarWords: ", wordToSimilarWords)
        # print("wordToSimilarWords['a']: ", wordToSimilarWords["a"])
        # print("wordToSimilarWords: ", wordToSimilarWords)
        for word1, word2 in similarPairs:
            wordToSimilarWords[word1].add(word2)
            wordToSimilarWords[word2].add(word1)
        print("wordToSimilarWords['great']: ", wordToSimilarWords["great"])
        print("wordToSimilarWords: ", wordToSimilarWords)
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or sentence2[i] in wordToSimilarWords[sentence1[i]]:
                continue
            return False
        return True



        # if sentence1 == sentence2:
        #     return True
        # if len(sentence1) != len(sentence2):
        #     return False

        # key_dict = {}
        # for i in range(len(similarPairs)):
        #     # if similarPairs[i][0] not in key_dict:
        #     # print("similarPairs[i]: ", similarPairs[i])
        #     key_dict[similarPairs[i][0]] = similarPairs[i][1]
        #     key_dict[similarPairs[i][1]] = similarPairs[i][0]
        # print("key_dict: ", key_dict)

        # for i in range(len(sentence1)):
        #     # if sentence1[i] in
        #     print("sentence2[i]: ", sentence2[i])
        #     print("sentence1[i]: ", sentence1[i])
        #     if sentence1[i] == sentence2[i] or sentence2[i] in key_dict[sentence1[i]] or sentence1[i] in key_dict[sentence2[i]]:
        #         print("continue")
        #         continue
        #     return False

        #     # print("key_dict[sentence1[i]]: ", key_dict[sentence1[i]])
        #     # print("key_dict[sentence2[i]]: ", key_dict[sentence2[i]])
        #     # if sentence1[i] == sentence2[i]:
        #     #     pass
        #     # else:
        #     #     if sentence2[i] not in key_dict or sentence1[i] not in key_dict:
        #     #         return False
        #     #     else:
        #     #         if sentence2[i] == key_dict[sentence1[i]]:
        #     #             pass
        #     #         elif sentence1[i] == key_dict[sentence2[i]]:
        #     #             pass
        #     #         else:
        #     #             return False
        # return True

def main(sentence1, sentence2, similarPairs):
    result = Solution()
    print(result.areSentencesSimilar(sentence1, sentence2, similarPairs))

if __name__== "__main__" :
    # sentence1 = ["great"]
    # sentence2 = ["doubleplus","good"]
    # similarPairs = [["great","doubleplus"]]
    # sentence1 = ["great","acting","skills"]
    # sentence2 = ["fine","drama","talent"]
    # similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
    # sentence1 = ["an","extraordinary","meal"]
    # sentence2 = ["one","good","dinner"]
    # similarPairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
    sentence1 = ["great","acting","skills"]
    sentence2 = ["fine","painting","talent"]
    similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
    # sentence1 = ["a","very","delicious","meal"]
    # sentence2 = ["one","really","delicious","dinner"]
    # similarPairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
    # sentence1 = ["this","summer","thomas","get","actually","actually","rich","and","possess","the","actually","great","and","fine","vehicle","every","morning","he","drives","one","nice","car","around","one","great","city","to","have","single","super","excellent","super","as","his","brunch","but","he","only","eat","single","few","fine","food","as","some","fruits","he","wants","to","eat","an","unique","and","actually","healthy","life"]
    # sentence2 = ["this","summer","thomas","get","very","very","rich","and","possess","the","very","fine","and","well","car","every","morning","he","drives","a","fine","car","around","unique","great","city","to","take","any","really","wonderful","fruits","as","his","breakfast","but","he","only","drink","an","few","excellent","breakfast","as","a","super","he","wants","to","drink","the","some","and","extremely","healthy","life"]
    # similarPairs = [["good","nice"],["good","excellent"],["good","well"],["good","great"],["fine","nice"],["fine","excellent"],["fine","well"],["fine","great"],["wonderful","nice"],["wonderful","excellent"],["wonderful","well"],["wonderful","great"],["extraordinary","nice"],["extraordinary","excellent"],["extraordinary","well"],["extraordinary","great"],["one","a"],["one","an"],["one","unique"],["one","any"],["single","a"],["single","an"],["single","unique"],["single","any"],["the","a"],["the","an"],["the","unique"],["the","any"],["some","a"],["some","an"],["some","unique"],["some","any"],["car","vehicle"],["car","automobile"],["car","truck"],["auto","vehicle"],["auto","automobile"],["auto","truck"],["wagon","vehicle"],["wagon","automobile"],["wagon","truck"],["have","take"],["have","drink"],["eat","take"],["eat","drink"],["entertain","take"],["entertain","drink"],["meal","lunch"],["meal","dinner"],["meal","breakfast"],["meal","fruits"],["super","lunch"],["super","dinner"],["super","breakfast"],["super","fruits"],["food","lunch"],["food","dinner"],["food","breakfast"],["food","fruits"],["brunch","lunch"],["brunch","dinner"],["brunch","breakfast"],["brunch","fruits"],["own","have"],["own","possess"],["keep","have"],["keep","possess"],["very","super"],["very","actually"],["really","super"],["really","actually"],["extremely","super"],["extremely","actually"]]
    main(sentence1, sentence2, similarPairs)
