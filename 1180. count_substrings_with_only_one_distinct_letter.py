class Solution:
    def countLetters(self, s: str) -> int:
        
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                print("i, j: ", i, j)
                print("temp: ", s[i:j])
                print("count: ", count)
                if s[i] != s[j]:
                    # print("temp: ", s[i:j])
                    # count += 1
                    break
                else:
                    count += 1
        print("count: ", count)

        return count

def main(s):
    result = Solution()
    print(result.countLetters(s))

if __name__== "__main__" :
    s = "aaaba"
    main(s)
