class Solution:
    def decodeString(self, s: str) -> str:

        # stack
        
        stack = []
        for char in s:
            if char == ']':
                decodedString = []
                # get the encoded string
                while stack[-1] != '[':
                    decodedString.append(stack.pop())
                # pop [ from the stack
                stack.pop()
                base = 1
                k = 0
                # get the number k
                while stack and stack[-1].isdigit():
                    k += int(stack.pop()) * base
                    base *= 10
                # decode k[decodedString], by pushing decodedString k times into stack
                while k != 0:
                    for ch in reversed(decodedString):
                        stack.append(ch)
                    k -= 1
            # push the current character to stack
            else:
                stack.append(char)
            print("stack: ", stack)

        # get the result from stack
        return ''.join(stack)

def main(s):
    result = Solution()
    print(result.minSteps(s))

if __name__== "__main__" :
    s = "3[a]2[bc]"
    main(s)
