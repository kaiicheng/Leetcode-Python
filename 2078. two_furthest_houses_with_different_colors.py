from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        mx = float("-inf")
        for i in range(len(colors)):
            for j in range(i + 1, len(colors)):
                # print("i, j: ", i, j)
                if colors[i] != colors[j]:
                    mx = max(j - i, mx)

        return mx

def main(colors):
    result = Solution()
    print(result.maxDistance(colors))

if __name__== "__main__" :
    colors = [1,1,1,6,1,1,1]
    main(colors)
