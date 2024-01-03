from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        ans = []

        for i in range(len(emails)):
            temp = emails[i].split("@")
            # print("temp: ", temp)
            local = temp[0]
            domain = temp[1]

            if "+" in local:
                local = local[:local.find("+")]
            # print("local, domain: ", local, domain)
        
            local = local.split(".")
            local = "".join(local)
            # print("local: ", local)

            # alternative
            # if "." in local:
            #     c = local.count(".")
            #     # print("c: ", c)
            #     for i in range(c):
            #         local = local.replace(".", "")
            #     # print("local: ", local)
            # # print("local, domain: ", local, domain)


            if local + "@" + domain not in ans:
                ans.append(local + "@" + domain)
        # print("ans: ", ans)
        return len(ans)

def main(emails):
    result = Solution()
    print(result.numUniqueEmails(emails))

if __name__== "__main__" :
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    main(emails)
