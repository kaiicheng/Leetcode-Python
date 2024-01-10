from typing import List

class Solution:
    def expand(self, s: str) -> List[str]:
        
        ls = []
        new_ls = []
        cur = []
        for i in range(len(s)):
            # print("i, s[i]: ", i, s[i])
            # print("ls: ", ls)
            # print("new_ls: ", new_ls)
            # print("cur: ", cur)
            if s[i] != ",":
                if s[i] =="}":
                    # print("1!")
                    # print("cur: ", cur)
                    if len(cur) > 0:
                        if len(ls) == 0:
                            for j in range(len(cur)):
                                ls.append(cur[j])
                            cur = []
                        else:
                            new_ls = []
                            for j in range(len(ls)):
                                for k in range(len(cur)):
                                    # print("j, k: ", j, k)
                                    # print("ls: ", ls)
                                    temp = []
                                    temp += ls[j]
                                    temp += cur[k]
                                    # print("temp: ", temp)
                                    # ls[j] = temp
                                    new_ls.append(temp)
                                    # print("ls: ", ls)
                            ls = new_ls
                            cur = []

                elif s[i] =="{":
                    # print("2!")
                    # print("cur: ", cur)
                    if len(cur) > 0:
                        if len(ls) == 0:
                            for j in range(len(cur)):
                                ls.append(cur[j])
                            cur = []
                        else:
                            new_ls = []
                            for j in range(len(ls)):
                                for k in range(len(cur)):
                                    # print("j, k: ", j, k)
                                    # print("ls: ", ls)
                                    temp = []
                                    temp += ls[j]
                                    temp += cur[k]
                                    # print("temp: ", temp)
                                    # ls[j] = temp
                                    new_ls.append(temp)
                                    # print("ls: ", ls)
                            ls = new_ls
                            cur = []
                else:
                    # print("3!")
                    # ls.append(s[i])
                    cur.append(s[i])
            # print("ls: ", ls)
            # print("new_ls: ", new_ls)
            # print("cur: ", cur)
            # print("---end of iteration---")
        
        if len(cur) > 0:
            if len(ls) == 0:
                ls.append(cur)
            else:
                new_ls = []
                for j in range(len(ls)):
                    for k in range(len(cur)):
                        # print("j, k: ", j, k)
                        # print("ls: ", ls)
                        temp = []
                        temp += ls[j]
                        temp += cur[k]
                        # print("temp: ", temp)
                        # ls[j] = temp
                        new_ls.append(temp)
                        # print("ls: ", ls)
                ls = new_ls
                cur = []
        # print("ls: ", ls)
        # print("new_ls: ", new_ls)

        for i in range(len(ls)):
            # print("i, ls[i]: ", i, ls[i])
            ls[i] = "".join(ls[i])
        
        ls.sort()
        return ls
    
def main(s):
    result = Solution()
    print(result.expand(s))

if __name__== "__main__" :
    s = "{a,b}c{d,e}f"
    main(s)
