# important! [:] is time consuming!

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        ans = 0
        # print(arr[:k])
        pre = arr[:k]
        pre_sum = sum(pre)
        if pre_sum / k >= threshold:
            ans += 1
        # print("pre, pre_sum: ", pre, pre_sum)

        for i in range(k, len(arr)):
            # print("i: ", i)
            # print("pre, pre_sum: ", pre, pre_sum)
            
            # important! [:] is time consuming!
            # pre.pop(0)
            # cur = pre + [arr[i]]
            
            cur_sum = pre_sum - arr[i - k] + arr[i]
            # print("cur_sum: ", cur_sum)
            
            avg = cur_sum / k
            # print("avg: ", avg)
            if avg >= threshold:
                ans += 1
            
            # pre = cur
            pre_sum = cur_sum
            # print("---end of iteration---")
        return ans



        # Time Limit Exceeded

        # ans = 0
        # for i in range(len(arr) - k + 1):
        #     # print("i, arr[i: i + k]: ", i, arr[i: i + k])
        #     cur = arr[i: i + k]
        #     avg = sum(cur) / len(cur)
        #     if avg >= threshold:
        #         ans += 1

        # return ans

def main(arr, k, threshold):
    result = Solution()
    print(result.numOfSubarrays(arr, k, threshold))

if __name__== "__main__" :
    arr = [11,13,17,23,29,31,7,5,2,3]
    k = 3
    threshold = 5
    main(arr, k, threshold)