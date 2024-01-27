class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        days = [None, 31,28,31,30,31,30,31,31,30,31,30,31]
        if month != 2:
            return days[month]
        y4 = year % 4 == 0
        y100 = year % 100 == 0
        y400 = year % 400 == 0
        if y4 and (not y100 or y400):
            return 29
        else:
            return 28

def main(year, month):
    result = Solution()
    print(result.numberOfDays(year, month))

if __name__== "__main__" :
    year = 1992
    month = 7
    main(year, month)
