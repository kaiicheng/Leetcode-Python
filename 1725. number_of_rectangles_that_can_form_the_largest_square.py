from typing import List
from collections import Counter

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        ls = []
        for i in range(len(rectangles)):
            ls.append(min(rectangles[i][0], rectangles[i][1]))
        # print("ls: ", ls)
        mx = max(ls)
        c = Counter(ls)
        return c[mx]

def main(rectangles):
    result = Solution()
    print(result.countGoodRectangles(rectangles))

if __name__== "__main__" :
    rectangles = [[5,8],[3,9],[5,12],[16,5]]
    main(rectangles)
