class Solution:
    def maskPII(self, s: str) -> str:

        # email
        if "@" in s:
            email = s.split("@")
            print("email: ", email)
            name = email[0].lower()
            domain = email[1].lower()
            name = name[0] + "*****" + name[-1]
            return name + "@" + domain

        # phone number
        else:
            separation = ["+", "-", "(", ")", " "] 
            for i in range(len(separation)):
                # print("separation[i]: ", separation[i])
                s = s.replace(separation[i], "")
            if len(s) == 13:
                s = "+" + "***" + "-" + "***" + "-" + "***" + "-" + s[9:]
            elif len(s) == 12:
                s = "+" + "**" + "-" + "***" + "-" + "***" + "-" + s[8:]
            elif len(s) == 11:
                s = "+" + "*" + "-" + "***" + "-" + "***" + "-" + s[7:]
            elif len(s) == 10:
                s = "***" + "-" + "***" + "-" + s[6:]
            # print("s: ", s)

            return s

def main(s):
    result = Solution()
    print(result.maskPII(s))

if __name__== "__main__" :
    s = "1(234)567-890"
    main(s)
