from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        # math equation
        # Sum(A) - x + y = Sum(B) - y + x => y = x + (Sum(B) - Sum(A))/2
        a = sum(aliceSizes)
        b = sum(bobSizes)

        s = set(bobSizes)

        for i in range(len(aliceSizes)):  
            if aliceSizes[i] + (b - a)/2 in s:
                return [aliceSizes[i], aliceSizes[i] + (b - a)//2]



        # Time Limit Exceeded
        # brute force

        # a = sum(aliceSizes)
        # b = sum(bobSizes)

        # ans = []
        # flag = False
        # for i in range(len(aliceSizes)):  
        #     for j in range(len(bobSizes)):
        #         # print("i, j: ", i, j)
        #         tar_a = a - aliceSizes[i]
        #         tar_b = b - bobSizes[j]
        #         # print("tar_a, tar_b: ", tar_a, tar_b)
        #         if tar_a + bobSizes[j] == tar_b + aliceSizes[i]:
        #             ans.append(aliceSizes[i])
        #             ans.append(bobSizes[j])
        #             flag = True
        #             break
        #     if flag:
        #         break
        # return ans

def main(aliceSizes, bobSizes):
    result = Solution()
    print(result.fairCandySwap(aliceSizes, bobSizes))

if __name__== "__main__" :
    aliceSizes = [1,1]
    bobSizes = [2,2]
    main(aliceSizes, bobSizes)
