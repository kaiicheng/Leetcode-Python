from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        c = Counter(arr)
        # print("c: ", c)

        item = list(c.items())
        item.sort(key=lambda x:x[1])
        # print("item: ", item)

        for i in range(len(item)):
            # print("i, item[i]: ", i, item[i])
            if k >= item[i][1]:

                if k >= item[i][1]:
                    temp = item[i][1]
                    item[i] = (item[i][0], item[i][1] - item[i][1])
                    k = k - temp
                elif k < item[i][1]:
                    temp = item[i][1]
                    item[i] = (item[i][0], item[i][1] - k)
                    k = temp - k
                # print("k: ", k)
            else:
                break

            if k == 0:
                break

        ans = 0
        for i in item:
            # print("i, i[1]: ", i, i[1])
            if i[1] > 0:
                ans += 1

        return ans


        # for i in item:
        #     print("i, i[0]: ", i, i[0])
        #     print("count: ", count)
        #     print("key: ", key)
        #     if count == k:
        #         break
        #     else:
        #         # del key[i[0]]
        #         print("i, i[0]: ", i, i[0])
        #         key.remove(i[0])
        #     count += 1

        # return len(key)



        # # Dictionary to track the frequencies of elements
        # freq_map = Counter(arr)

        # # List to track all the frequencies
        # frequencies = list(freq_map.values())

        # # Sorting the frequencies
        # frequencies.sort()

        # # Tracking the number of elements removed
        # elements_removed = 0

        # for i in range(len(frequencies)):
        #     # Removing frequencies[i] elements, which equates to
        #     # removing one unique element
        #     elements_removed += frequencies[i]

        #     # If the number of elements removed exceeds k, return
        #     # the remaining number of unique elements
        #     if elements_removed > k:
        #         return len(frequencies) - i

        # # We have removed all elements, so no unique integers remain
        # # Return 0 in this case
        # return 0

def main(arr, k):
    result = Solution()
    print(result.findLeastNumOfUniqueInts(arr, k))

if __name__== "__main__" :
    arr = [4,3,1,1,3,3,2]
    k = 3
    main(arr, k)

