from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        di = {}

        for i in range(len(indices)):
            di[indices[i]] = s[i]
        # print("di: ", di)
        ls = list(di.items())
        ls.sort()
        # print("ls: ", ls)

        ans = [i[1] for i in ls]
        # print("ans: ", ans)
        return "".join(ans)

def main(s, indices):
    result = Solution()
    print(result.restoreString(s, indices))

if __name__== "__main__" :
    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    main(s, indices)
