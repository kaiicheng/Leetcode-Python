class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        
        # print("len(num): ", len(num))

        index = 0
        for i in reversed(num):
            # print("i: ", i)
            if i != "0":
                break
            index += 1

        return num[:len(num) - index]

        # .strip()
        
        # return num.strip('0')

def main(num):
    result = Solution()
    print(result.removeTrailingZeros(num))

if __name__== "__main__" :
    num = "51230100"
    main(num)
