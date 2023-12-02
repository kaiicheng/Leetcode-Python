from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for i in range(n):
            times = i + 1
            print("times: ", times)
            if times % 3 == 0 and times % 5 == 0:
                ans.append("FizzBuzz")
            elif times % 3 == 0 and times % 5 != 0:
                ans.append("Fizz")
            elif times % 3 != 0 and times % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(times))
        return ans

if __name__== "__main__" :
    n = 5
    result = Solution()
    print(result.fizzBuzz(n))