class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        l = 0
        mx = 0
        for r in range(1, len(s) + 1):
            
            # print("l, r: ", l, r)
            
            cur_str = s[l:r]
            # print("cur_str: ", cur_str)

            freq = set(cur_str)
            # print("freq: ", freq)

            if len(freq) <= k:
                mx = max(mx, len(cur_str))
            elif len(freq) > k:
                # print("---over k!---")
                while len(set(s[l:r])) > k:
                    # print("l, r: ", l, r)
                    # print("s[l:r]: ", s[l:r])
                    l += 1

        return mx

def main(s, k):
    result = Solution()
    print(result.lengthOfLongestSubstringKDistinct(s, k))

if __name__== "__main__" :
    s = "aa"
    k = 1
    main(s, k)