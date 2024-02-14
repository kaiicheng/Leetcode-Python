from typing import List

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        ans = []
        if len(currentState) < 2:
            return []
        else:
            for i in range(len(currentState) - 1):
                if currentState[i] == "+" and currentState[i + 1] == "+":
                    temp = currentState[:i] + "--" + currentState[i + 2:]
                    ans.append(temp)
                    # print("temp: ", temp)
        return ans

def main(currentState):
    result = Solution()
    print(result.generatePossibleNextMoves(currentState))

if __name__== "__main__" :
    currentState = "++++"
    main(currentState)
