# ord() to get ASCII code
# c = 'p'
# print("The ASCII value of '" + c + "' is", ord(c))  #112

class Solution:
    def sortVowels(self, s: str) -> str:
        
        v = "aeiouAEIOU"

        ans = []
        temp = []
        for i in range(len(s)):
            if s[i] not in v:
                ans.append(s[i])
            else:
                ans.append("")
                temp.append([ord(s[i]), s[i]])
        temp.sort()
        # print("ans, temp: ", ans, temp)

        temp_i = 0
        for i in range(len(ans)):
            if ans[i] == "":
                # print("i, temp_i: ", i, temp_i)
                ans[i] = temp[temp_i][1]
                temp_i += 1
        # print("ans: ", ans)
        return "".join(ans)

def main(s):
    result = Solution()
    print(result.sortVowels(s))

if __name__== "__main__" :
    s = "lEetcOde"
    main(s)
