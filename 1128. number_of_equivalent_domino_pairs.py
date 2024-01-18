# temp = dominoes[j].reverse()                    
# print("temp: ", temp)  # temp is None

from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        ans = 0
        dic = {}

        for i in dominoes:
            d = tuple(sorted(i))
            if d in dic:
                dic[d] += 1
            else:
                dic[d] = 1
        
        # print("dic: ", dic)

        # now check for count of pairs
        # step 2: caculate the pairs. for each pair, number of pairs = n*(n-1)//2
        for v in dic.values():
            # print("v: ", v)
            s = v * (v-1)//2
            ans += s

        return ans            



        # Time Limit Exceeded

        # ans = 0
        # for i in range(len(dominoes)):
        #     cur = dominoes[i]
        #     for j in range(len(dominoes)):
        #         if i < j:
        #             # print("i, j: ", i, j)
        #             # temp = dominoes[j].reverse()  # temp is None
        #             temp = dominoes[j][::-1]
        #             # print("cur, dominoes[j], temp: ", cur, dominoes[j], temp)
        #             if cur == dominoes[j] or cur == temp:
        #                 # print("cur, dominoes[j]: ", cur, dominoes[j])
        #                 ans += 1
        # return ans

def main(dominoes):
    result = Solution()
    print(result.numEquivDominoPairs(dominoes))

if __name__== "__main__" :
    dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    main(dominoes)
