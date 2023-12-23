from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        mx = 0
        cur = 0
        for i in range(len(gain)):
            cur += gain[i]
            mx = max(cur, mx)
        return mx
    
def main(gain):
    result = Solution()
    print(result.largestAltitude(gain))

if __name__== "__main__" :
    gain = [-4,-3,-2,-1,4,3,2]
    main(gain)
