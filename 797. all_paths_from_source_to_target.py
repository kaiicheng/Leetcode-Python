from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        # backtracking

        # target = len(graph) - 1
        # results = []

        # def backtrack(curr_node, path):
        #     print("curr_node, path: ", curr_node, path)
        #     # if we reach the target, no need to explore further.
        #     if curr_node == target:
        #         results.append(list(path))
        #         return
        #     # explore the neighbor nodes one after another.
        #     for next_node in graph[curr_node]:
        #         path.append(next_node)
        #         backtrack(next_node, path)
        #         path.pop()
        # # kick of the backtracking, starting from the source node (0).
        # path = [0]
        # backtrack(0, path)

        # return results



        di = {}
        start = 0
        end = len(graph) - 1
        for i in range(len(graph)):
            di[i] = graph[i]
        # print("di: ", di)
        # print("di[0]: ", di[0])

        ans = []
        cur = []
        def go(node, start, end, cur):
            # print("node, start, end, cur: ", node, start, end, cur)
            # print("ans: ", ans)
            if cur[-1] == end:
                # ans.append(cur)

                # important! need to append list(cur) instead of cur!
                ans.append(list(cur))
                # print("ans: ", ans)
                return
            # print("di[node]: ", di[node])

            # path = [start]
            for i in range(len(di[node])):
                cur.append(di[node][i])
                go(di[node][i], start, end, cur)
                
                # important! Need to pop the last element added!
                cur.pop()

        go(0, start, end, [0])
        # print("ans: ", ans)
        return ans

def main(nums, k):
    result = Solution()
    print(result.allPathsSourceTarget(nums, k))

if __name__== "__main__" :
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    main(graph)
