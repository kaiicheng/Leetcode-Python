from collections import Counter

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        c = Counter(s)
        # print("c[letter]: ", c[letter])

        return int((c[letter] / len(s)) * 100)

def main(s, letter):
    result = Solution()
    print(result.percentageLetter(s, letter))

if __name__== "__main__" :
    s = "foobar"
    letter = "o"
    main(s, letter)