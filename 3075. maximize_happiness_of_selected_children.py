from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort(reverse=True)
        # print("happiness: ", happiness)
        # print("happiness[:k]: ", happiness[:k])
        
        happiness = happiness[:k]
        # print("happiness: ", happiness)
        
        ans = 0
        # print("ans: ", ans)
        
        neg = 0
        for i in range(k):
            # print("neg: ", neg)
            if i == 0:
                ans += happiness[i]
                pass
            else:
                neg += 1
                # print("neg: ", neg)
                # print("i: ", i)
                # print("happiness[i]: ", happiness[i])
                
                if happiness[i] - neg < 0:
                    break
                else:
                    ans += happiness[i] - neg

        return ans
        
        
#         TLE
#         # happiness = (set(happiness))
#         # print("happiness: ", happiness)
        
#         happiness.sort(reverse=True)
#         # print("happiness: ", happiness)
        
#         ans = 0
#         mx_index = 0
#         for j in range(k):
#             mx = happiness[mx_index]
#             happiness[mx_index] = 0
#             # print("mx, mx_index: ", mx, mx_index)
#             ans += mx

#             for i in range(len(happiness)):
#                 if i == mx_index:
#                     pass
#                 else:
#                     if happiness[i] - 1 >= 0:
#                         happiness[i] -= 1
#                     else:
#                         pass
#                 # print("happiness: ", happiness)
#                 # print("ans: ", ans)
#             mx_index += 1
#         # print("---end---")
#         return ans

def main(happiness, k):
    result = Solution()
    print(result.maximumHappinessSum(happiness, k))

if __name__== "__main__" :
    happiness = [1,2,3]
    k = 2
    main(happiness, k)
