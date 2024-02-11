from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        
        ans = 0
        m_plus = len(pattern) + 1
        for i in range(len(nums) - m_plus + 1):
            # print("i: ", i)
            cur = nums[i:i + m_plus]
            # print("cur: ", cur)
            valid = True
            for j in range(len(pattern)):
                # print("pattern[j]: ", pattern[j])
                # print("j, cur[j], cur[j + 1]: ", j, cur[j], cur[j + 1])
                if pattern[j] == 1:
                    if cur[j + 1] > cur[j]:
                        pass
                    else:
                        valid = False
                        break
                elif pattern[j] == 0:
                    if cur[j + 1] == cur[j]:
                        pass
                    else:
                        valid = False
                        break
                elif pattern[j] == -1:
                    if cur[j + 1] < cur[j]:
                        pass
                    else:
                        valid = False
                        break
            if valid:
                ans += 1
            # print("ans: ", ans)

        return ans

def main(nums, pattern):
    result = Solution()
    print(result.countMatchingSubarrays(nums, pattern))

if __name__== "__main__" :
    nums = [1,4,4,1,3,5,5,3]
    pattern = [1,0,-1]
    main(nums, pattern)