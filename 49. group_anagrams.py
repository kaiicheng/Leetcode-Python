# python tuple
# print("tuple('are'): ", tuple('are'))  # ('a', 'r', 'e')

# Time Limit Exceeded for list

# TypeError: unhashable type: 'Counter'
#     if c not in di_c:

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # print(Counter({'e': 1, 'a': 1, 't': 1}) == Counter({'t': 1, 'e': 1, 'a': 1}))  # True

        print("tuple('are'): ", tuple('are'))  # ('a', 'r', 'e')


        ans = collections.defaultdict(list)
        print("ans: ", ans)
        for s in strs:
            print("s: ", s)
            print("tuple(s): ", tuple(s))
            ans[tuple(sorted(s))].append(s)
        print("ans: ", ans)
        return ans.values()


        # wrong
        # TypeError: unhashable type: 'Counter'

        # # ls_c = []
        # di_c = {}
        # ans = []
        # for i in range(len(strs)):
        #     # if Counter(strs[i]) not in di:
        #     # print("strs[i]: ", strs[i])
        #     c = Counter(strs[i])
        #     # print("Counter(strs[i]): ", c)
            
        #     if c not in di_c:
        #         # ls_c.append(c)
        #         di_c[c] = ""
        #         ans.append([strs[i]])
        #     elif c in di_c:
        #         ls_c = list(di_c)
        #         index = ls_c.index(c)
        #         ans[index].append(strs[i])
        # # print("ls_c: ", ls_c)
        # return ans

def main(strs):
    result = Solution()
    print(result.groupAnagrams(strs))

if __name__== "__main__" :
    strs = ["eat","tea","tan","ate","nat","bat"]
    main(strs)
