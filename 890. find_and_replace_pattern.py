# Counter.items()
# Counter.keys()
# Counter.values()

from typing import List
from collections import Counter

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        c_pattern = Counter(pattern)
        c_pattern_val = c_pattern.values()
        # print("c_pattern_val: ", c_pattern_val)

        def find_permutation(str):
            di = {}
            start_i = 97  # ord("a") = 97
            temp = ""
            for i in range(len(str)):
                if str[i] not in di:
                    di[str[i]] = start_i
                    temp += chr(start_i)
                    start_i += 1
                else:
                    temp += chr(di[str[i]])
            # print("temp: ", temp)
            return temp

        permutation = find_permutation(pattern)  # abab

        ans = []
        for i in range(len(words)):
            c_word = Counter(words[i])
            c_word_val = c_word.values()
            # print("c_word_val: ", c_word_val)

            if list(c_word_val) == list(c_pattern_val) and find_permutation(words[i]) == permutation:
                ans.append(words[i])

        # print("ans: ", ans)

        return ans

def main(arr):
    result = Solution()
    print(result.peakIndexInMountainArray(arr))

if __name__== "__main__" :
    arr = [0,10,5,2]
    main(arr)
