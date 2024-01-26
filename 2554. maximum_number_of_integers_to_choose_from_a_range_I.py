from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        # accelerate
        banned = set(banned)

        cur = []
        total = 0
        for i in range(1, n + 1):
            if i not in banned and total + i <= maxSum:
                cur.append(i)
                total += i
            elif i not in banned and total + i > maxSum:
                break
            elif total == maxSum:
                break
        return len(cur)

def main(banned, n, maxSum):
    result = Solution()
    print(result.maxCount(banned, n, maxSum))

if __name__== "__main__" :
    banned = [1,6,5]
    n = 5
    maxSum = 6
    main(banned, n, maxSum)
