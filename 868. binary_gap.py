class Solution:
    def binaryGap(self, n: int) -> int:
        
        bi = bin(n)[2:]
        # print("bi: ", bi)

        # for i in range(len(bi)):
        l = 0
        mx = 0
        while l < len(bi):
            if bi[l] != "0":
                for r in range(l + 1, len(bi)):
                    # print("l, r: ", l, r)
                    if bi[r] == "1":
                        mx = max(mx, r - l)
                        break
                # print("mx: ", mx)
            # else:
            #     l += 1
            l += 1
        return mx

def main(n):
    result = Solution()
    print(result.binaryGap(n))

if __name__== "__main__" :
    n = 22
    main(n)
