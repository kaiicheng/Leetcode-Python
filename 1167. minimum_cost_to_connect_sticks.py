from typing import List

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        if len(sticks) == 1:
            return 0

        sticks.sort()
        # print("sticks: ", sticks)

        cost = 0
        # cur = copy.deepcopy(sticks)
        cur = sticks
        while len(cur) > 1:
            # print("cur: ", cur)
            one = cur[0]
            two = cur[1]
            cost += one + two
            cur.remove(one)
            cur.remove(two)

            cur.insert(0, one + two)
            cur.sort()

            # wrong

            # print("one + two: ", one + two)
            # print("cur: ", cur)
            # for i in range(len(cur)):
            #     print("i, cur[i]: ", i, cur[i])
            #     if one + two <= cur[i]:
            #         cur.insert(i, one + two)
            #         break                
            #     elif one + two >= cur[i]:
            #         cur.insert(i, one + two)
            #         break

        # print("cur: ", cur)
        return cost

def main(sticks):
    result = Solution()
    print(result.connectSticks(sticks))

if __name__== "__main__" :
    sticks = [3354,4316,3259,4904,4598,474,3166,6322,8080,9009]
    main(sticks)
