from typing import List
from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        
        ans = 0
        
        freq = "".join(words)
        freq = Counter(freq)
        # print("freq: ", freq)
        
        even = 0
        odd = 0
        for i in freq.values():
            even += i // 2 * 2
            odd += i % 2
        print("even, odd: ", even, odd)
        
        l = [len(i) for i in words]
        l.sort()
        # print("l: ", l)

        for i in l:
            # a = i // 2 * 2
            
            len_odd = i % 2  # odd
            len_even = i - len_odd  # even
            print("len_odd, len_even: ", len_odd, len_even)

            # aaaabbbb => freq = [4, 4] => [aaaa, bb, bb]
            if even >= len_even and odd >= len_odd:
                even -= len_even
                odd -= len_odd
                ans += 1

            # aabb => freq = [2, 2] => [a, a, bb]
            # break 1 even into 2 odd
            elif even >= len_even and even - len_even + odd >= len_odd:
                even -= len_even
                len_odd -= odd
                odd = 0
                even -= len_odd
                ans += 1
            # print("ans: ", ans)

        return ans
                
#         wrong
        
#         # di = defaultdict
#         di = {}
#         for i in range(len(words)):
#             for j in range(len(words[i])):
#                 if j + 1 not in di:
#                     s = set()
#                     s.add(words[i][j])
#                     di[j + 1] = s
#                 else:
#                     temp = di[j + 1]
#                     temp.add(words[i][j])
#                     di[j + 1] = temp
#         print("di: ", di)

        
#         for i in range(len(words)):         
#             for j in range(len(words[i])):
                
                
        # return -1

def main(words):
    result = Solution()
    print(result.maxPalindromesAfterOperations(words))

if __name__== "__main__" :
    words = ["a","a","bb"]
    main(words)