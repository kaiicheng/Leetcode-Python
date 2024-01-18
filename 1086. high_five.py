from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        data = []
        visited_stu = []
        for i in range(len(items)):
            # print("data: ", data)
            stu = items[i][0]
            sco = items[i][1]
            # print("stu, sco: ", stu, sco)
            if stu not in visited_stu:
                data.append([stu, [sco]])
            else:
                for j in range(len(data)):
                    if data[j][0] == stu:
                        data[j][1].append(sco)
            visited_stu.append(stu)
        print("data: ", data)

        ans = []
        for i in range(len(data)):
            stu = data[i][0]
            sco = data[i][1]
            sco.sort()
            avg = sum(sco[-5:])//5
            ans.append([stu, avg])
        ans.sort()
        return ans

def main(items):
    result = Solution()
    print(result.expand(items))

if __name__== "__main__" :
    items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    main(items)
