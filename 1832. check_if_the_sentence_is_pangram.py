from collections import Counter

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        ls = list(sentence)
        c = Counter(ls)
        if len(c) == 26:
            return True
        else:
            return False

def main(nums):
    result = Solution()
    print(result.minStartValue(nums))

if __name__== "__main__" :
    nums = [-3,2,-3,4,2]
    main(nums)
