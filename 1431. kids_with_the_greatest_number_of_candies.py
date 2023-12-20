from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        ans = []
        for i in range(len(candies)):
            mx = max(candies)
            if candies[i] + extraCandies >= mx:
                ans.append(True)
            else:
                ans.append(False)
        return ans
    
def main(candies, extraCandies):
    result = Solution()
    print(result.kidsWithCandies(candies, extraCandies))

if __name__== "__main__" :
    candies = [2,3,5,1,3]
    extraCandies = 3
    main(candies, extraCandies)
