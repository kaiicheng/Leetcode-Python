class Solution:
    def maximum69Number(self, num: int) -> int:
        
        n = str(num)
        n = [i for i in n]
        # print("n: ", n)

        for i in range(len(n)):
            if n[i] == "6":
                n[i] = "9"
                break
        # print("n: ", n)

        return int("".join(n))

def main(num):
    result = Solution()
    print(result.maximum69Number(num))

if __name__== "__main__" :
    num = 9669
    main(num)
