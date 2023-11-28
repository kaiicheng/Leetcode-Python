import copy

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_main = {}
        a = copy.deepcopy(s)
        b = copy.deepcopy(t)

        for i in range(len(a)):
            # print("i: ", i)
            # print("a[i]: ", a[i])
            # print("list(dict_main.values()): ", list(dict_main.values()))
            if a[i] in dict_main:
                if dict_main[a[i]] != b[i]:
                    return False
            else:
                # print("!b[i]: ", b[i])
                if b[i] in list(dict_main.values()):
                    return False
                dict_main[a[i]] = b[i]
            # print(dict_main)
        return True

if __name__== "__main__" :
    # s = "egg"
    # t = "add"
    # s = "foo"
    # t = "bar"
    # s = "paper"
    # t = "title"
    s = "badc"
    t = "baba"

    result = Solution()
    print(result.isIsomorphic(s, t))
