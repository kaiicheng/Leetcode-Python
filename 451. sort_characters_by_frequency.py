from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        
        s = [i for i in s]
        # print("s: ", s)
        
        c = Counter(s)
        c = list(c.items())
        c.sort(key=lambda x: x[1], reverse=True)
        # print("c: ", c)

        ans = []
        for i in c:
            for j in range(i[1]):
                ans.append(i[0])

        return "".join(ans)

def main(s):
    result = Solution()
    print(result.frequencySort(s))

if __name__== "__main__" :
    s = "cccaaa"
    main(s)
