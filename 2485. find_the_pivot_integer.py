# review
class Solution:
    def pivotInteger(self, n: int) -> int:

        ls = [i for i in range(1, n + 1)]
        # print("ls: ", ls)
        total = sum(ls)

        cur_sum = 0
        back_sum = total
        ans = -1
        for i in range(len(ls)):
            # print("i, cur_sum, back_sum: ", i, cur_sum, back_sum)
            cur_sum += ls[i]
            if cur_sum == back_sum:
                ans = i + 1
                break
            back_sum -= ls[i]

        return ans

def main(n):
    result = Solution()
    print(result.pivotInteger(n))

if __name__== "__main__" :
    n = 8
    main(n)
