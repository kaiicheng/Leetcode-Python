from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def check(num):
            digit = []
            for i in range(len(str(num))):
                digit.append(str(num)[i])
            # print("digit: ", digit)
            for i in range(len(digit)):
                if int(digit[i]) == 0:
                    return False
                else:
                    if num % int(digit[i]) != 0:
                        return False
            return True 

        ans = []
        for i in range(left, right + 1):
            # print("i: ", i)
            if check(i):
                ans.append(i)
        return ans

def main(a, b):
    result = Solution()
    print(result.selfDividingNumbers(a, b))

if __name__== "__main__" :
    left = 1
    right = 22
    main(left, right)
