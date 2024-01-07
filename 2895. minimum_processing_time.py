from typing import List

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        processorTime.sort()
        tasks.sort()
        ans = 0

        for i in processorTime:
            ans = max(ans, i + max(tasks[-4:]))
            tasks = tasks[:-4]
        return ans

def main(processorTime, tasks):
    result = Solution()
    print(result.minProcessingTime(processorTime, tasks))

if __name__== "__main__" :
    processorTime = [8,10]
    tasks = [2,2,3,1,8,7,4,5]
    main(processorTime, tasks)
