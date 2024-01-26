from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ls = []

        for i in range(len(points)):
            dist = points[i][0] ** 2 + points[i][1] ** 2
            # print("dist: ", dist)
            ls.append([dist, points[i]])
        ls.sort()
        # print("ls: ", ls)

        ans = [ ls[i][1] for i in range(len(ls)) if i <= k - 1]
        # print("ans: ", ans)
        return ans

def main(points, k):
    result = Solution()
    print(result.kClosest(points, k))

if __name__== "__main__" :
    points = [[1,3],[-2,2]]
    k = 1
    main(points, k)
