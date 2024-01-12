class Solution:
    def sumOfMultiples(self, n: int) -> int:

        ls = []
        for i in range(1, n + 1):
            # print("i: ", i)
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                ls.append(i)
        return sum(ls)

def main(n):
    result = Solution()
    print(result.sumOfMultiples(n))

if __name__== "__main__" :
    n = 10
    main(n)
