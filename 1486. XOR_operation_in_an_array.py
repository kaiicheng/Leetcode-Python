class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        arr = [start + 2 * i for i in range(n)]
        # print("arr: ", arr)

        first = arr[0]
        for i in range(1, len(arr)):
            first ^= arr[i]

        return first

def main(n, start):
    result = Solution()
    print(result.xorOperation(n, start))

if __name__== "__main__" :
    n = 5
    start = 0
    main(n, start)
