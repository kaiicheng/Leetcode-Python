from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        def check(i, j, mat):
            # print("1! in i, j: ", i, j)
            # print("mat, len(mat): ", mat, len(mat))
            for k in range(len(mat)):
                for l in range(len(mat[k])):
                    # print("k, l: ", k, l)
                    if k == i and l == j:
                        pass
                    else:
                        # print("In! k, l: ", k, l)
                        # print("mat[l], mat[l][i], mat[k][l]:", mat[l], mat[l][i], mat[k][l])
                        if k == i:
                            if mat[k][l] == 1:
                                # print("!false!")
                                return False
                        if l == j:
                            if mat[k][l] == 1:
                                # print("!false!")
                                return False
            return True

        ans = 0
        result = False
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                # print("i, j: ", i, j)
                if mat[i][j] == 1:
                    result = check(i, j, mat)
                    # print("result: ", result)
                if result:
                    ans += 1
                    result = False
                # print("---end of iteration---")
        return ans



        # wrong
        
        # ans = 0
        # zero = None

        # for i in range(len(mat)):
        #     for j in range(len(mat[i])):
        #         print("i, j: ", i, j)

        #         for k in range(len(mat)):
        #             zero = 0
        #             for l in range(len(mat[i])):
        #                 print("k, l: ", k, l)
        #                 print("mat[l], mat[l][i], mat[k][l]:", mat[l], mat[l][i], mat[k][l])
        #                 if i != j:
        #                     if mat[l][i] != 0 or mat[k][l] != 0:
        #                         break
        #                     else:
        #                         ans += 1
        # return ans
    
def main(mat):
    result = Solution()
    print(result.numSpecial(mat))

if __name__== "__main__" :
    mat = [[1,0,0],[0,0,1],[1,0,0]]
    main(mat)
