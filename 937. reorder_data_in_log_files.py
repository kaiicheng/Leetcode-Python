# print("art can", "art can".isalpha(): ", "art can", "art can".isalpha())  # "art can", False

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letter = []
        digit = []

        for i in range(len(logs)):

            cur = logs[i].split()
            iden = cur[0]
            # print("iden: ", iden)
            rest = "".join(cur[1:])
            # print("rest, rest.isdigit(): ", rest, rest.isdigit())

            if rest.isdigit():
                digit.append(logs[i])
            else:
                # logs[i].split()
                # print("iden len(iden): ", iden, len(iden))
                # print("logs[i][len(iden):]: ", logs[i][len(iden):])
                letter.append([logs[i][len(iden):], logs[i]])

        # letter.sort(key=lambda x: x[3])
        # print("letter: ", letter)
        letter.sort()
        # print("letter: ", letter)
        letter = [i[1] for i in letter]
        # print("letter: ", letter)
        # print("digit: ", digit)

        return letter + digit

def main(logs):
    result = Solution()
    print(result.reorderLogFiles(logs))

if __name__== "__main__" :
    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    main(logs)
