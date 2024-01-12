class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        ls = [i for i in range(1, n + 1)]
        # print("ls: ", ls)

        i = time % (n - 1)
        side = time // (n - 1)
        print("i, side: ", i, side)

        if side % 2 == 0:
            return ls[i]
        elif side % 2 == 1:
            return ls[-1 * i - 1]

def main(n, time):
    result = Solution()
    print(result.passThePillow(n, time))

if __name__== "__main__" :
    n = 4
    time = 5
    main(n, time)
