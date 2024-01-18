from typing import List

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:

        ans = []
        num = []
        for i in range(n):
            for j in range(n - 1):
                # print("i + 1, j + 1: ", i + 1, j + 1)
                # print("(j + 1) / (i + 1): ", (j + 1) / (i + 1))
                if (j + 1) / (i + 1) < 1 and (j + 1) / (i + 1) not in num:
                    ans.append(str(j + 1) + "/" + str(i + 1))
                    num.append((j + 1) / (i + 1))
        # print("ans: ", ans)

        return ans

def main(n):
    result = Solution()
    print(result.simplifiedFractions(n))

if __name__== "__main__" :
    n = 4
    main(n)
