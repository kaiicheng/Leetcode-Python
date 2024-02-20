from typing import List

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:

        special.sort()
        ls = []

        if bottom < special[0]:
            ls.append([bottom, special[0] - 1])

        for i in range(1, len(special)):
            # print("i: ", i)
            if special[i - 1] + 1 <= special[i] - 1:
                ls.append([special[i - 1] + 1, special[i] - 1])
            # print("ls: ", ls)

        if special[-1] < top:
            ls.append([special[-1] + 1, top])
        # print("ls: ", ls)

        ans = []
        for i in range(len(ls)):
            # print("ls: ", ls)
            ans.append(ls[i][1] - ls[i][0] + 1)
        # print("ans: ", ans)

        if len(ans) == 0:
            return 0
        else:
            return max(ans)



        # Time Limit Exceeded

        # special.sort()

        # if top - bottom + 1 == len(special):
        #     return 0

        # mx = 0
        # c = 0
        # for i in range(bottom, top + 1):
        #     # print("i: ", i)
        #     # print("c: ", c)
        #     if i in special:
        #         mx = max(mx, c)
        #         c = 0
        #     else:
        #         c+= 1
        #     # print("---")

        # mx = max(mx, c)

        # return mx

def main(bottom, top, special):
    result = Solution()
    print(result.maxConsecutive(bottom, top, special))

if __name__== "__main__" :
    bottom = 6
    top = 8
    special = [7,6,8]
    main(bottom, top, special)
