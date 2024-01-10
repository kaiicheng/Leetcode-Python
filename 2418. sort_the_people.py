from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        ls = []
        for i in range(len(names)):
            ls.append([heights[i], names[i]])
        ls.sort(reverse=True)

        ans = [ls[i][1] for i in range(len(ls))]
        return ans

def main(names, heights):
    result = Solution()
    print(result.sortPeople(names, heights))

if __name__== "__main__" :
    names = ["Mary","John","Emma"]
    heights = [180,165,170]
    main(names, heights)
