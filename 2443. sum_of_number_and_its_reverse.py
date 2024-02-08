import copy

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        
        if num == 0:
            return True

        x = 1
        while x < num:
            x_str = copy.deepcopy(str(x))
            x_str_rev = x_str[::-1]
            # print("x_str, x_str_rev: ", x_str, x_str_rev)
            if int(x_str) + int(x_str_rev) == num:
                return True
            # elif int(x_str) + int(x_str_rev) > num:
            #     break
            x += 1

        return False

def main(num):
    result = Solution()
    print(result.sumOfNumberAndReverse(num))

if __name__== "__main__" :
    num = 443
    main(num)
