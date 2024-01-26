from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        print(skill)

        pre = skill[0] + skill[-1]
        ans = skill[0] * skill[-1]
        for i in range(1, len(skill) // 2):
            # print("i, len(skill) - i: ", i, len(skill) - i - 1)
            # print("pre, skill[i] + skill[len(skill) - i - 1]: ", pre, skill[i] + skill[len(skill) - i - 1])
            if skill[i] + skill[len(skill) - i - 1] != pre:
                return -1
            ans += skill[i] * skill[len(skill) - i - 1]
        return ans

def main(skill):
    result = Solution()
    print(result.dividePlayers(skill))

if __name__== "__main__" :
    skill = [3,2,5,1,3,4]
    main(skill)
