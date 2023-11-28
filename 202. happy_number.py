import copy

class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(copy.deepcopy(n))
        visited_num = []

        while num != "1":
            ans = 0
            for i in range(len(num)):
                ans += int(num[i]) ** 2
            if ans in visited_num:
                break
            visited_num.append(ans)
            num = str(ans)

        if num == "1":
            return True
        else:
            return False

if __name__== "__main__" :
    # n = 19
    n = 2
    result = Solution()
    print(result.isHappy(n))

