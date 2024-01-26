from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        
        c = Counter(word)
        result = Counter(word)
        # print("c: ", c)
        
        # c= sorted(c, key=c.get, reverse=True)
        # print("c: ", c)
        
        ls = list(reversed(c.most_common()))
        # ls.sort(ls, key=lambda ls: ls[1])
        ls = sorted(ls, key=lambda x: x[1], reverse=True)
        # print("ls: ", ls)
#         c.most_common()
#         print("c: ", c)
        
        ans = 0
        times = 1
        
        eight = 1
        for i in range(len(ls)):
            # for j in range(result[i]):
            #     # print("result: ", result)
            #     print("i, j: ", i, j)
            # print("c.most_common(i): ", c.most_common(i))
            
            # print("i, ls[i], eight, times, ans: ", i, ls[i], eight, times, ans)
            

            ans += 1 * (ls[i][1]) * times
            if eight == 8:
                eight = 0
                times += 1
            # del ls[i]
            # print("ls: ", ls)
            eight += 1

            # print("---end of iteration---")
        return ans

def main(word):
    result = Solution()
    print(result.minimumPushes(word))

if __name__== "__main__" :
    word = "abcde"
    main(word)
