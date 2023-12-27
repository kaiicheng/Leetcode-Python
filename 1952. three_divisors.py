# print(1.0 == 1)  # True

class Solution:
    def isThree(self, n: int) -> bool:

        ls = []
        for i in range(1, n + 1):
            # print("i: ", i)
            # print("n / i, n // i: ", n / i, n // i)
            if n / i == n // i:
                if int(i) not in ls:
                    ls.append(int(i))
                if int(n / i) not in ls:
                    ls.append(int(n/i))
        # print("ls, len(ls): ", ls, len(ls))
        if len(ls) == 3:
            return True
        else:
            return False

def main(n):
    result = Solution()
    print(result.isThree(n))

if __name__== "__main__" :
    n = 4
    main(n)
