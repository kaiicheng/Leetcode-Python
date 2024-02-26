from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        # Convert the string to a list of characters for in-place modification
        s = list(s)
        n = len(shifts)
        print("s, n: ", s, n)

        # Accumulate shifts in reverse order
        for i in range(n - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        print("shifts: ", shifts)
        
        # Apply the shifts to each character
        for i in range(n):
            # Calculate the new character code with modulo to wrap around 'z'
            new_code = (ord(s[i]) - ord('a') + shifts[i]) % 26 + ord('a')
            s[i] = chr(new_code)
        
        # Join the list back into a string
        return ''.join(s)



        # Time Limit Exceeded

        # s = [i for i in s]
        # # print("s: ", s)

        # ans = []

        # for i in range(len(shifts)):
        #     # print("shifts[i]: ", shifts[i])
        #     for j in range(i + 1):
        #         # print("s[j], ord(s[j]): ", s[j], ord(s[j]))
        #         temp = ord(s[j]) + shifts[i]
        #         # print("temp, chr(temp): ", temp, chr(temp))
        #         while temp > 122:
        #             temp -= 26
        #             # print("temp, chr(temp): ", temp, chr(temp))
        #         s[j] = chr(temp)
        #         # print("s: ", s)
        #         # print("---iteration---")
                
        # return "".join(s)

def main(s, shifts):
    result = Solution()
    print(result.shiftingLetters(s, shifts))

if __name__== "__main__" :
    s = "abc"
    shifts = [3,5,9]
    main(s, shifts)
