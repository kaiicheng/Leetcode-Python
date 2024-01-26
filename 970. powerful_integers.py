from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        ans = []
        i1 = 0
        i2 = 0

        if x == 1 and y == 1:
            i1 = 1
            i2 = 1
        else:
            if x == 1:
                i1 = 1
                while y ** i2 <= bound:
                    i2 += 1
                    if y ** i2 > bound:
                        i2 -= 1
                        break
            elif y == 1:
                i2 = 1
                while x ** i1 <= bound:
                    i1 += 1
                    if x ** i1 > bound:
                        i1 -= 1
                        break
            if x != 1 and y != 1:
                while x ** i1 <= bound:
                    i1 += 1
                    if x ** i1 > bound:
                        i1 -= 1
                        break

                while y ** i2 <= bound:
                    i2 += 1
                    if y ** i2 > bound:
                        i2 -= 1
                        break

        # print("i1, i2: ", i1, i2)

        for i in range(i1 + 1):
            for j in range(i2 + 1):
                # print("i, j: ", i, j)
                if x ** i + y ** j <= bound and x ** i + y ** j not in ans:
                    ans.append(x ** i + y ** j)
        # print("ans: ", ans)
        return ans



        # wrong

        # if x ** i1 + y ** i2 <= bound:
        #     ans.append(x ** i1 + y ** i2)

        # while x ** i1 + y ** i2 <= bound:
        #     print("i1, i2: ", i1, i2)
        #     print("x ** i1 + y ** i2: ", x ** i1 + y ** i2)

        #     if x ** (i1 + 1) + y ** i2 <= bound:
        #         if x ** (i1 + 1) + y ** i2 not in ans:
        #             ans.append(x ** (i1 + 1) + y ** i2)
        #     if x ** i1 + y ** (i2 + 1) <= bound:
        #         if x ** i1 + y ** (i2 + 1) not in ans:
        #             ans.append(x ** i1 + y ** (i2 + 1))
        #     i1 += 1
        #     i2 += 1
        #     print("ans: ", ans)

        # print("ans: ", ans)
        # return ans

def main(x, y, bound):
    result = Solution()
    print(result.powerfulIntegers(x, y, bound))

if __name__== "__main__" :
    x = 2
    y = 3
    bound = 10
    main(x, y, bound)
