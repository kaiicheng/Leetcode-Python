from typing import List
from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check row
        for i in range(len(board)):
            c = Counter(board[i])
            # print("c: ", c)
            for j in c:
                if j is not ".":
                    if c[j] > 1:
                        return False

        # check column
        for i in range(len(board[0])):
            cur = []
            for j in range(len(board)):
                # print("j, i: ", j, i)
                cur.append(board[j][i])
            # print("cur: ", cur)
            c = Counter(cur)
            # print("c: ", c)
            for j in c:
                if j is not ".":
                    if c[j] > 1:
                        return False
        
        # check 3 x 3 sub-boxes
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                
                # print("i, j: ", i, j)
                cur = []
                for l in range(i, i + 2 + 1, 1):
                    for m in range(j, j + 2 + 1, 1):
                        # print("l, m: ", l, m)
                        cur.append(board[l][m])
                # print("cur: ", cur)
                c = Counter(cur)
                # print("c: ", c)
                for j in c:
                    if j is not ".":
                        if c[j] > 1:
                            return False

        return True

def main(board):
    result = Solution()
    print(result.isValidSudoku(board))

if __name__== "__main__" :
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    main(board)
