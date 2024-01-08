# list.pop(index)
# del list[index]
# list.remove(value)

from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        
        mx = max(salary)
        mi = min(salary)

        salary.remove(mx)
        salary.remove(mi)

        return sum(salary) / len(salary)

def main(salary):
    result = Solution()
    print(result.average(salary))

if __name__== "__main__" :
    salary = [4000,3000,1000,2000]
    main(salary)
