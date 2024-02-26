from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # reverse each row
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
            # print("matrix[i]: ", matrix[i])

        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                # print("i, j: ", i, j)
                # print("matrix[i][j]: ", matrix[i][j])
                # print("set: ", set)
                if (i, j) not in visited:
                    visited.add((i, j))
                    # print("len(matrix) - j - 1, len(matrix[i]) - i - 1: ", len(matrix) - j - 1, len(matrix[i]) - i - 1)
                    visited.add((len(matrix) - j - 1, len(matrix[i]) - i - 1))
                    temp = matrix[len(matrix) - j - 1][len(matrix[i]) - i - 1]
                    # print("temp: ", temp)
                    matrix[len(matrix) - j - 1][len(matrix[i]) - i - 1] = matrix[i][j]
                    matrix[i][j] = temp
                    
                    # print("matrix: ", matrix)
                    # print("---iteration---")

        return matrix

def main(matrix):
    result = Solution()
    print(result.rotate(matrix))

if __name__== "__main__" :
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    main(matrix)
