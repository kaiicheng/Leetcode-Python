from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        prev = 0
        ans = 0

        for s in bank:

            count = s.count('1')

            if count > 0:
                ans += prev * count
                prev = count

        return ans

def main(bank):
    result = Solution()
    print(result.numberOfBeams(bank))

if __name__== "__main__" :
    bank = ["011001","000000","010100","001000"]
    main(bank)
