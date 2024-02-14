# di = {1: [1, 2, 3]}
# print("di: ", di)  # di:  {1: [1, 2, 3]}

from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        # di = defaultdict(int)
        di = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in di:
                di[groupSizes[i]] = [i]
            else:
                di[groupSizes[i]].append(i)
        # print("di: ", di)

        ans = []
        for i in di:
            ls = di[i]
            temp = []
            for j in range(len(ls)):
                # print("i, j, ls[j]: ", i, j, ls[j])
                # print("temp: ", temp)
                # print("ans: ", ans)
                temp.append(ls[j])
                if len(temp) == i:
                    ans.append(temp)
                    temp = []
        return ans



        # wrong

        # groupSizes.sort()
        # print("groupSizes: ", groupSizes)
        
        # ans = []
        # temp = [groupSizes[0]]
        # for i in range(1. len(groupSizes)):
        #     if groupSizes[0] ==         
        #         ans.append()

        # return ans

def main(groupSizes):
    result = Solution()
    print(result.groupThePeople(groupSizes))

if __name__== "__main__" :
    groupSizes = [3,3,3,3,3,1,3]
    main(groupSizes)
