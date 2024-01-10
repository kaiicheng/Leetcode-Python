from typing import List
import collections

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        # use an array to store frequencies
        remainders = collections.defaultdict(int)
        ans = 0
        for t in time:
            # print("t: ", t)

            # check if a % 60==0 && b % 60==0
            if t % 60 == 0: 
                ans += remainders[0]
            # check if a%60 + b%60==60
            else:
                # print("remainders: ", remainders)
                ans += remainders[60 - t % 60]
                # print("remainders: ", remainders)
            remainders[t % 60] += 1 # remember to update the remainders

            # print("remainders: ", remainders)
            # print("ans: ", ans)
        return ans



        # wrong 
        # hashmap

        # di = {element: index for index, element in enumerate(time)}
        # # print("di: ", di)

        # ans = 0
        # for i in range(len(time)):
        #     if time[i] 
        # return ans



        # Time Limit Exceeded
        # two pointer

        # ans = 0
        # l = 0
        # while l < len(time):
        #     for r in range(l + 1, len(time)):
        #         # print("l, r: ", l, r)
        #         # print("time[l], time[r], time[l] + time[r]: ", time[l], time[r], time[l] + time[r])
        #         if (time[l] + time[r]) % 60 == 0:
        #             ans += 1
        #         # print("ans: ", ans)
        #     l += 1
        # return ans

def main(time):
    result = Solution()
    print(result.numPairsDivisibleBy60(time))

if __name__== "__main__" :
    time = [30,20,150,100,40]
    main(time)
