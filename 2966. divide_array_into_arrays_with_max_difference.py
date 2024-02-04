from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        print("nums: ", nums)
    
        count = 1
        ans = []
        ls = []
        for i in range(len(nums)):
            # print("i: ", i)
            if count == 3:
                ls.append(nums[i])
                print("ls: ", ls)
                if max(ls) - min(ls) > k:
                    return []
                ans.append(ls)
                count = 0
                ls = []
            else:
                ls.append(nums[i])
            count +=1
        
        return ans

def main(nums, k):
    result = Solution()
    print(result.divideArray(nums, k))

if __name__== "__main__" :
    nums = [1,3,4,8,7,9,3,5,1]
    k = 2
    main(nums, k)
