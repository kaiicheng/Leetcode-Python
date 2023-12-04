# 202 in base 7 representation
# 2 * 7 ^ 2 + 0 * 7 ^ 1 + 2 * 7 ^ 0 = 98 + 2 = 100

class Solution:
    def convertToBase7(self, num: int) -> str:
        
        negative = False

        if num < 0:
            negative = True
            num = num * -1

        n = num
        times = 0
        while num > 0:
        # for _ in range(10):
            if n > 7 ** times:
                times += 1
            elif n == 7 ** times:
                break
            else:
                times -= 1
                break
        print("times: ", times)
        print("n: ", n)

        ans = ""
        for i in range(times + 1):
            print("i: ", i)
            print("times: ", times)
            print("num: ", num)

            x = 0
            while num >= x * 7 ** times:
                x += 1
                print("x: ", x)
            x -= 1
            ans = ans + str(x)

            num = num - x * 7 ** times
            times -= 1

            print("ans: ", ans)
            # n = (num / (7 ** times)) - res

            # res = num - n * 7 ** times

        if negative:
            ans = int(ans) * (-1)
        
        # print("ans: ", ans)
        return str(ans)

def main(words):
    result = Solution()
    print(result.convertToBase7(words))

if __name__== "__main__" :
    # num = 100
    # num = 49
    num = -7
    main(num)
