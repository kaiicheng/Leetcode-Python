# sorted(l, key=lambda k: (float(k['score']), -k['id']), reverse=True)
# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]
# sorted(student_tuples, key=lambda student: student[2])   # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# sort array by length
# arr.sort(key=len)

# capitalize() method returns a string where the first character is upper case, and the rest is lower case.
# .capitalize()

class Solution:
    def arrangeWords(self, text: str) -> str:
        
        # student_tuples = [
        #     ('john', 'A', 15),
        #     ('jane', 'B', 12),
        #     ('dave', 'B', 10),
        # ]
        # print(sorted(student_tuples, key=lambda student: student[2]))   # sort by age



        a = []
        for x in text.split(" "):
            a.append(x.lower())
        # print("a: ", a)
        # print("' '.join(sorted(a, key=len)).capitalize(): ", " ".join(sorted(a, key=len)).capitalize())
        return " ".join(sorted(a, key=len)).capitalize()



        # # convert string to an array
        # arr = text.split()
        # # convert the first letter of the array to a lower case letter
        # arr[0] = arr[0].lower()
        # # sort array by length
        # arr.sort(key=len)
        # # convert the first letter of the array to an upper case letter
        # arr[0] = arr[0].capitalize()
        # # convert array to string
        # return " ".join(arr)



        # wrong

        # text = text.split(" ")

        # ls = []
        # for i in range(len(text)):
        #     ls.append([len(text[i]), text[i]])
        # ls.sort()
        # print("ls: ", ls)

        # return ""

def main(text):
    result = Solution()
    print(result.arrangeWords(text))

if __name__== "__main__" :
    text = "Leetcode is cool"
    main(text)
