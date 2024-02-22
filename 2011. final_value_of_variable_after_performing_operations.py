from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        start = 0
        for i in range(len(operations)):

            if operations[i] == "++X" or operations[i] == "X++":
                start += 1
            elif operations[i] == "--X" or operations[i] == "X--":
                start -= 1
        return start

def main(operations):
    result = Solution()
    print(result.finalValueAfterOperations(operations))

if __name__== "__main__" :
    operations = ["--X","X++","X++"]
    main(operations)
