# find index of element in list

# ["foo", "bar", "baz"].index("bar")  # 1

class Solution:
    def reformatDate(self, date: str) -> str:

        m_ls = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date = date.split(" ")
        # print("date: ", date)
        day = date[0]
        for i in range(len(day)):
            # print("i, day[i]: ", i, day[i])
            if day[i].isdigit() != True:
                day = day[: i]
                break
        if len(day) < 2:
            day = "0" + day

        # print("day: ", day)

        month = date[1]
        month = str(m_ls.index(month) + 1)
        if len(month) < 2:
            month = "0" + month

        # print("month: ", month)
        year = date[2]
        # print("year: ", year)

        ans = str(year) + "-" + str(month) + "-" + str(day)
        return ans
        


        # ans = ''
        # date = date.split()
        # for i in date[0]:
        #     if i.isdigit():
        #         ans += i
        # if len(ans) == 1:
        #     ans = '0' + ans
        # ans = '-' + ans
        # l = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        # ans = '0' * (l.index(date[1])+1 < 10) + str(l.index(date[1])+1) + ans
        # ans = '-' + ans
        # ans = str(date[2]) + ans
        # return ans

def main(date):
    result = Solution()
    print(result.reformatDate(date))

if __name__== "__main__" :
    date = "20th Oct 2052"
    main(date)
