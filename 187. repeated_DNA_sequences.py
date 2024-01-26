from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        # Linear-time Slice Using Substring + HashSet

        # L, n = 10, len(s)     
        # seen, output = set(), set()

        # # iterate over all sequences of length L
        # for start in range(n - L + 1):
        #     tmp = s[start:start + L]
        #     if tmp in seen:
        #         output.add(tmp[:])
        #     seen.add(tmp)
        # return output



        di = {}
        ans = []
        for i in range(len(s) - 10 + 1):
            # print("i: ", i)
            # print("s[i: i + 10]: ", s[i: i + 10])
            cur_s = s[i: i + 10]
            if cur_s not in di:
                di[cur_s] = ""
            elif cur_s in di and cur_s not in ans:
                ans.append(cur_s)
            # print("di: ", di)
            # print("ans: ", ans)
        return ans

def main(s):
    result = Solution()
    print(result.findRepeatedDnaSequences(s))

if __name__== "__main__" :
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    main(s)
