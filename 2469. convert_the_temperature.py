class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        k = celsius + 273.15
        f = celsius * 1.80 + 32.00

        return [k, f]

def main(celsius):
    result = Solution()
    print(result.convertTemperature(celsius))

if __name__== "__main__" :
    celsius = 36.50
    main(celsius)
