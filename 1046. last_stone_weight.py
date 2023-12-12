from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1:
            return stones[0]

        s = stones
        while len(s) > 1 :
            s.sort()
            print("s: ", s)

            y = s[-1]
            x = s[-2]

            s = s[:-2]

            if x == y:
                pass
            else:
                s.append(y - x)

        # print("s: ", s)

        if len(s) == 0:
            return 0
        else:
            return s[0]

def main(stones):
    result = Solution()
    print(result.lastStoneWeight(stones))

if __name__== "__main__" :
    stones = [2,7,4,1,8,1]
    main(stones)
