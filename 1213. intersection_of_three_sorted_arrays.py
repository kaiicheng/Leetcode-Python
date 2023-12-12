# set can create a random order non-repeating set
# x = set('eleven')
# y = set('twelve')
# x, y
# ({'l', 'e', 'n', 'v'}, {'e', 'v', 'l', 't', 'w'})
# x & y
# {'l', 'e', 'v'}
# x | y
# {'e', 'v', 'n', 'l', 't', 'w'}
# x - y
# {'n'}
# y - x
# {'t', 'w'}
# x ^ y (not common element)
# {'t', 'n', 'w'}
# y ^ x (not common element)
# {'w', 'n', 't'}

# Counter(list1 + list2 + list3s)
# Counter({1: 3, 5: 3, 2: 2, 3: 2, 4: 2, 7: 1, 9: 1, 8: 1})

from typing import List
from collections import Counter

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        # Set

        # temp = set(arr2) + set(arr3)
        # ans = set(arr1).union(set(arr2))
        ans = set(arr1) & set(arr2)
        ans = ans & set(arr3)
        # print(ans)
        ans = list(ans)
        ans.sort()
        return ans



        # Counter

        # counter = Counter(arr1 + arr2 + arr3) # concatenate them together
        # print("counter: ", counter)

        # ans = []

        # for item in counter:
        #     if counter[item] == 3:
        #         ans.append(item)
        # return ans



        # dictionary

        # di_1 = {}
        # di_2 = {}
        # di_3 = {}
        
        # n = max(len(arr1), len(arr2), len(arr3))
        
        # for i in range(n):
        #     if i < len(arr1):
        #         if arr1[i] not in di_1:
        #             di_1[arr1[i]] = 1
        #         else:
        #             di_1[arr1[i]] += 1

        #     if i < len(arr2):
        #         if arr2[i] not in di_2:
        #             di_2[arr2[i]] = 1
        #         else:
        #             di_2[arr2[i]] += 1

        #     if i < len(arr3):
        #         if arr3[i] not in di_3:
        #             di_3[arr3[i]] = 1
        #         else:
        #             di_3[arr3[i]] += 1
        
        # print("di_1: ", di_1)
        # print("di_2: ", di_2)
        # print("di_3: ", di_3)

        # ans = []

        # for i in range(len(arr1)):
        #     if arr1[i] in di_2 and arr1[i] in di_3:
        #         ans.append(arr1[i])
        # print("ans: ", ans)

        # return ans

def main(arr1, arr2, arr3):
    result = Solution()
    print(result.arraysIntersection(arr1, arr2, arr3))

if __name__== "__main__" :
    arr1 = [1,2,3,4,5]
    arr2 = [1,2,5,7,9]
    arr3 = [1,3,4,5,8]
    main(arr1, arr2, arr3)
