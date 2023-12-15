from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        di = {}
        for i in range(len(paths)):
            if paths[i][0] not in di:
                di[paths[i][0]] = 1
        print("di: ", di)
        for i in range(len(paths)):
            print("paths[i][1]: ", paths[i][1])
            if paths[i][1] not in di:
                return paths[i][1]
            
def main(paths):
    result = Solution()
    print(result.destCity(paths))

if __name__== "__main__" :
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    main(paths)
