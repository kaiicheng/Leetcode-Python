# string.replace() will replace all matching characters

# print("1100011".replace("0", "1"))  # 1111111

class Solution:
    def maximumTime(self, time: str) -> str:
        
        hour, minute = time.split(":")
        # print("hour, minute: ", hour, minute)

        if "?" in hour:
            # print("hour.find('?'): ", hour.find("?"))
            if hour.find("?") == 0:
                if hour[1] != "?" and int(hour[1]) >= 4:
                    hour = "1" + hour[1]
                else:
                    hour = "2" + hour[1]
            if hour.find("?") == 1:
                if hour[0] == "1" or hour[0] == "0":
                    hour = hour[0] + "9"
                elif hour[0] == "2":
                    hour = hour[0] + "3"
        if "?" in minute:
            # print("minute.find('?'): ", minute.find("?"))
            # print("hour, minute: ", hour, minute)
            if minute.find("?") == 0:
                minute = "5" + minute[1]

            if minute.find("?") == 1:
                minute = minute[0] + "9"

        return hour + ":" +  minute

def main(time):
    result = Solution()
    print(result.maximumTime(time))

if __name__== "__main__" :
    time = "??:??"
    main(time)
