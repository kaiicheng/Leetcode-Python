# 3i + 3 = num
# i + 1 = num/3
# i = num/3 - 1

from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        if num % 3 != 0:
            return []
        else:
            ans = num // 3 - 1
            # print("ans: ", ans)
        return [ans, ans + 1, ans + 2]


        # Time Limit Exceeded

        # start = (num // 3) - 1
        # print("start: ", start)

        # for i in range(start, num):
        #     if i + (i + 1) + (i + 2) == num:
        #         return [i, i + 1, i + 2]



        # wrong

        # for i in range(1, num):
        #     for j in range(i + 1, num):
        #         for k in range(j + 1, num):
        #             if i + j + k == num:
        #                 return [i, j, k]

def main(num):
    result = Solution()
    print(result.sumOfThree(num))

if __name__== "__main__" :
    num = 33
    main(num)
