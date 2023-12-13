from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        odd = 0
        even = 0
        for i in range(len(position)):
            if position[i] % 2 == 0:
                even += 1
            else:
                odd += 1
        print("odd, even: ", odd, even)

        return min(odd, even)

def main(position):
    result = Solution()
    print(result.pivotIminCostToMoveChips(position))

if __name__== "__main__" :
    position = [2,2,2,3,3]
    main(position)
