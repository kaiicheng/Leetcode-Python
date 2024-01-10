from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        depth = 0
        for i in range(len(logs)):
            if logs[i] == "../":
                depth -= 1
                if depth < 0:
                    depth = 0
            elif logs[i] == "./":
                pass
            else:
                depth += 1
            
        return depth

def main(logs):
    result = Solution()
    print(result.minOperations(logs))

if __name__== "__main__" :
    logs = ["d1/","d2/","./","d3/","../","d31/"]
    main(logs)
