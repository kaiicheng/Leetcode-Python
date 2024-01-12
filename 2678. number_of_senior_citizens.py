from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        ans = 0
        for i in range(len(details)):
            age = details[i][9 + 1 + 1: 9 + 1 + 2 + 1]
            # print("age: ", age)
            if int(age) > 60:
                ans += 1
        return ans

def main(details):
    result = Solution()
    print(result.countSeniors(details))

if __name__== "__main__" :
    details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
    main(details)
