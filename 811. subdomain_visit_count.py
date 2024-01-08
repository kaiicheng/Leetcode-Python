from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        di = {}
        for i in range(len(cpdomains)):
            sent = cpdomains[i].split(" ")
            time = sent[0]
            domains = sent[1]
            # domains = domains.split(".")
            # print("time, domains: ", time, domains)

            for i in range(domains.count(".") + 1):
                # print("i: ", i)
                if domains in di:
                    di[domains] += int(time)
                else:
                    di[domains] = int(time)
                # print("domains: ", domains)
                domains = domains[domains.find(".") + 1:]
                # print("domains: ", domains)
                # print("di: ", di)
            # print("---end of iteration---")           
        # print("di: ", di)

        ans = []
        for i in di:
            ans.append(str(di[i]) + " " + i)
        # print("ans: ", ans)

        return ans

def main(cpdomains):
    result = Solution()
    print(result.subdomainVisits(cpdomains))

if __name__== "__main__" :
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    main(cpdomains)
