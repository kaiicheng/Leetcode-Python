class Solution:
    def interpret(self, command: str) -> str:
        
        # di = {"G": "G", "()": "o", "(al)": "al"}
        ans = []
        for i in range(len(command)):
            if command[i] == "G":
                ans.append("G")
            elif command[i] == ")":
                if command[i - 1] == "l":
                    ans.append("al")
                elif command[i - 1] == "(":
                    ans.append("o")
            elif command[i] == "(":
                pass
        return "".join(ans)
    
def main(command):
    result = Solution()
    print(result.interpret(command))

if __name__== "__main__" :
    command = "G()()()()(al)"
    main(command)
