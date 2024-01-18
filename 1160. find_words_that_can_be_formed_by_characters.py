from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        c = Counter(chars)
        # print("c: ", c)

        ans = 0
        for i in range(len(words)):

            cur_c = Counter(words[i])
            # print("cur_c: ", cur_c)

            yes = True
            for j in cur_c:
                # print("j: ", j)
                # print("j not in c, cur_c[j] > c[j]: ", j not in c, cur_c[j] >= c[j])
                if j not in c or cur_c[j] > c[j]:
                    yes = False
                    break
            if yes:
                ans += len(words[i])

        return ans

def main(words, chars):
    result = Solution()
    print(result.countCharacters(words, chars))

if __name__== "__main__" :
    words = ["cat","bt","hat","tree"]
    chars = "atach"
    main(words, chars)
