from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        
        c = Counter(word)
        result = Counter(word)
        # print("c: ", c)
        
        ans = 0
        times = 1
        eight = 0
        for i in result:
            if eight == 8:
                eight = 0
                times += 1
            ans += 1 * times
            del c[i]
            # print("c: ", c)
            eight += 1
        return ans

def main(word):
    result = Solution()
    print(result.minimumPushes(word))

if __name__== "__main__" :
    word = "abcde"
    main(word)
