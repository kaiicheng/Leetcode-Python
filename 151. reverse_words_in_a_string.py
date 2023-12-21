# for loop one line
# ans = [ls[i] for i in range(len(ls)) if ls[i] != '']

class Solution:
    def reverseWords(self, s: str) -> str:
        
        ls = s.split(" ")
        ls.reverse()
        print("ls: ", ls)

        # one line
        ans = [ls[i] for i in range(len(ls)) if ls[i] != '']

        # wrong 
        # ls = [i if i != "" else pass for i in range(len(ls))]
        # ls = [ls[i] if i != "" else print(ls[i]) for i in range(len(ls))]

        # alternative

        # ans = []
        # for i in range(len(ls)):
        #     print("ls[i]: ", ls[i])
        #     if ls[i] != '':
        #         ans.append(ls[i])
        #     else: 
        #         pass
        
        print("ans: ", ans)
        ans = " ".join(ans)
        ans = ans.strip()
        # print("ans: ", ans)
        return ans

def main(s):
    result = Solution()
    print(result.reverseWords(s))

if __name__== "__main__" :
    s = "a good   example"
    main(s)
