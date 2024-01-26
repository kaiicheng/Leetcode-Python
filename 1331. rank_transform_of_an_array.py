from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        di = {}
        for i in range(len(arr)):
            if arr[i] not in di:
                di[arr[i]] = [i]
            elif arr[i] in di:
                di[arr[i]].append(i)
        # print("di: ", di)

        ls = list(di.items())
        ls.sort()
        # print("ls: ", ls)

        rank = 1
        di = {}
        for i in range(len(ls)):
            di[ls[i][0]] = rank
            rank += 1
        # print("di: ", di)

        for i in range(len(arr)):
            arr[i] = di[arr[i]]

        return arr

        # ans = copy.deepcopy(arr)
        # rank = 1
        # for i in range(len(ls)):
        #     # print("ls[i], ls[i][0], ls[i][1]: ", ls[i], ls[i][0], ls[i][1])
        #     # print("rank: ", rank)
        #     for j in range(len(arr)):
        #         # print("i, j: ", i, j)
        #         # print("ls[i][0], arr[j]: ", ls[i][0], arr[j])
        #         if ls[i][0] == arr[j]:
        #             # print("found!")
        #             ans[j] = rank
        #         # print("---end of iteration---")
        #     rank += 1
        # return ans



        # ls = []
        # for i in range(len(arr)):
        #     ls.append([i + 1, arr[i]])
        # print("ls: ", ls)
        
        # arr.sort(reverse = True)
        # print("ls: ", ls)
        
        # ls.sort(key = lambda x: x[1], reverse = True)
        # print("ls: ", ls)

def main(arr):
    result = Solution()
    print(result.arrayRankTransform(arr))

if __name__== "__main__" :
    arr = [40,10,20,30]
    main(arr)
