from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        s = 0
        for i in nums:
            s += i if i % 2 == 0 else 0
        print("s: ", s)

        ans = []

        for i in queries:
            if nums[i[1]] % 2 == 0: 
                s -= nums[i[1]]
            nums[i[1]] += i[0]
            if nums[i[1]] % 2 == 0:
                s += nums[i[1]]
            ans.append(s)

        return ans



        # Time Limit Exceeded

        # ans = []

        # for i in range(len(queries)):
        #     # temp = copy.deepcopy(nums)
        #     nums[queries[i][1]] = nums[queries[i][1]] + queries[i][0]
        #     # print("nums: ", nums)
            
        #     # cur_sum = [i for i in nums if i% 2 == 0]
        #     # ans.append(sum(cur_sum))
        
        #     cur_sum = 0
        #     for i in nums:
        #         if i% 2 == 0:
        #             cur_sum += i
        #     ans.append(cur_sum)
        # return ans

def main(nums, queries):
    result = Solution()
    print(result.sumEvenAfterQueries(nums, queries))

if __name__== "__main__" :
    nums = [1,2,3,4]
    queries = [[1,0],[-3,1],[-4,0],[2,3]]
    main(nums, queries)
