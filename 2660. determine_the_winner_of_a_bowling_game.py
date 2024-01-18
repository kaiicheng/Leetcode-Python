from typing import List

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
        s1 = 0
        s2 = 0
        for i in range(len(player1)):
            # print("i, player1[i]: ", i, player1[i])
            # print("i - 1, player1[i - 1]: ", i - 1, player1[i - 1])
            # print("i - 2, player1[i - 2]: ", i - 2, player1[i - 2])
            if i - 2 < 0 and i - 1 < 0:
                s1 += player1[i]
                s2 += player2[i]

            elif i - 2 < 0 and i - 1 >= 0:
                if player1[i - 1] == 10:
                    s1 += player1[i] * 2
                else:
                    s1 += player1[i]
                if player2[i - 1] == 10:
                    s2 += player2[i] * 2
                else:
                    s2 += player2[i]
            elif i - 2 >= 0 and i - 1 >= 0:
                if player1[i - 2] == 10 or player1[i - 1] == 10:
                    s1 += player1[i] * 2
                else:
                    s1 += player1[i]
                if player2[i - 2] == 10 or player2[i - 1] == 10:
                    s2 += player2[i] * 2
                else:
                    s2 += player2[i]
            # print("s1, s2: ", s1, s2)

        # print("s1, s2: ", s1, s2)

        if s1 > s2:
            return 1
        elif s1 < s2:
            return 2
        elif s1 == s2:
            return 0
    
def main(player1, player2):
    result = Solution()
    print(result.isWinner(player1, player2))

if __name__== "__main__" :
    player1 = [4,10,7,9]
    player2 = [6,5,2,3]
    main(player1, player2)
