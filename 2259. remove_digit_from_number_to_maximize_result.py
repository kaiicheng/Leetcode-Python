class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        ls = []
        
        for i in range(len(number)):
            if number[i] == digit:
                ls.append(int(number[:i] + number[i + 1:]))
        return str(max(ls))

def main(number, digit):
    result = Solution()
    print(result.removeDigit(number, digit))

if __name__== "__main__" :
    number = "551"
    digit = "5"
    main(number, digit)
