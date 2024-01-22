# score.sort(key=lambda x: x[k], reverse=True)

from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        
        # score.sort(key=lambda score: score[k], reverse=True)
        score.sort(key=lambda x: x[k], reverse=True)
        # print("score: ", score)

        return score

def main(score, k):
    result = Solution()
    print(result.sortTheStudents(score, k))

if __name__== "__main__" :
    score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
    k = 2
    main(score, k)
