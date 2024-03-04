# "a" => 97
# "0210".lstrip("0") => "210"

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        ls1 = list(firstWord)
        ls2 = list(secondWord)
        ls3 = list(targetWord)
        # print("ls1, ls2, ls3: ", ls1, ls2, ls3)

        s1 = []
        s2 = []
        s3 = []

        for i in range(len(ls1)):
            s1.append(str(ord(ls1[i]) - 97))
        # print("s1, s2, s3: ", s1, s2, s3)
        s1 = "".join(s1)
        s1 = s1.lstrip("0")
        if s1 == '':
            s1 = '0'

        for i in range(len(ls2)):
            s2.append(str(ord(ls2[i]) - 97))
        # print("s1, s2, s3: ", s1, s2, s3)
        s2 = "".join(s2)
        s2 = s2.lstrip("0")
        if s2 == '':
            s2 = '0'

        for i in range(len(ls3)):
            s3.append(str(ord(ls3[i]) - 97))
        # print("s1, s2, s3: ", s1, s2, s3)
        s3 = "".join(s3)
        s3 = s3.lstrip("0")
        if s3 == '':
            s3 = '0'

        # print("s1, s2, s3: ", s1, s2, s3)

        if int(s1) + int(s2) == int(s3):
            return True
        else:
            return False

def main(firstWord, secondWord, targetWord):
    result = Solution()
    print(result.isSumEqual(firstWord, secondWord, targetWord))

if __name__== "__main__" :
    firstWord = "acb"
    secondWord = "cba"
    targetWord = "cdb"
    main(firstWord, secondWord, targetWord)
