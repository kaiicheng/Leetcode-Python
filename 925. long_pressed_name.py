class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        

        i, j = 0, 0
        while j < len(typed):

            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j-1] == typed[j]:
                j += 1
            else:
                return False
            print("i, j: ", i, j)

        return i == len(name)

        # wrong

        # pointer = 0
        # for i in range(len(name)):
        #     print("---start---")
        #     print("i, pointer: ", i, pointer)
        #     print("name[i], typed[pointer]: ", name[i], typed[pointer])

        #     if name[i] != typed[pointer]:
        #         print("!False!")
        #         print("name[i], typed[pointer]: ", name[i], typed[pointer])
        #         return False

        #     # pointer = i

        #     while pointer < len(typed):
        #         if pointer == len(typed) - 1:
        #             break
        #         else:
        #             print("pointer + 1, typed[pointer + 1]: ", pointer + 1, typed[pointer + 1])
        #             pointer += 1
        #             print("i, name[i]:　", i, name[i])
        #             if name[i] != typed[pointer]:
        #                 print("!break!")
        #                 break
        # return True

def main(name, typed):
    result = Solution()
    print(result.isLongPressedName(name, typed))

if __name__== "__main__" :
    name = "saeed"
    typed = "ssaaedd"
    main(name, typed)
