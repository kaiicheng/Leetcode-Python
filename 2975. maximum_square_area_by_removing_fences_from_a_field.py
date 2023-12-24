from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        
        hFences.sort()
        vFences.sort()
        
        hFences.insert(0, 1)
        vFences.insert(0, 1)
        hFences.append(m)
        vFences.append(n)
        # print("hFences, vFences: ", hFences, vFences)
        
        mx = -1
        
        h = {}
        for i in range(len(hFences)):
            for j in range(i, len(hFences)):
                # print("i, j, hFences[i], hFences[j]: ", i, j, hFences[i], hFences[j])
                if hFences[j] - hFences[i] > 0 and hFences[j] - hFences[i] not in h:
                    # print("h in!")
                    h[hFences[j] - hFences[i]] = []
                
                # if hFences[i] == vFences[j]:
                #     print("1!")
                #     mx = max(mx, hFences[i] * vFences[j])
              
        w = {}
        for i in range(len(vFences)):
            for j in range(i, len(vFences)):
                # print("i, j, vFences[i], vFences[j]: ", i, j, vFences[i], vFences[j])
                if vFences[j] - vFences[i] > 0 and vFences[j] - vFences[i] not in w:
                    # print("w in!")
                    w[vFences[j] - vFences[i]] = ""
                    if vFences[j] - vFences[i] in h:
                        mx = max(mx, (vFences[j] - vFences[i]) ** 2)
                
        # print("h, w: ", h, w)
        
        # mx = -1
        # for i in h:
        #     for j in w:
        #         if i == j:
        #             mx = max(mx, i * j)
        

        # alternative
        # MOD = int(1e9 + 7)
        # if mx != -1:
        #     return mx % MOD
        # else:
        #     return -1

        return mx % int(1e9+7) if mx != -1 else -1

def main(m, n, hFences, vFences):
    result = Solution()
    print(result.maximizeSquareArea(m, n, hFences, vFences))

if __name__== "__main__" :
    m = 6
    n = 7
    hFences = [2]
    vFences = [4]
    main(m, n, hFences, vFences)





        
#         hFences.sort()
#         vFences.sort()
        
        
#         if m == n:
#             return (m - 1) * (n - 1)     

#         mx = -1
#         height = m
#         width = n
        
#         hFences.insert(0, 0)
#         vFences.insert(0, 0)
#         hFences.append(m)
#         vFences.append(n)
#         print("hFences, vFences: ", hFences, vFences)

#         for i in range(1, len(hFences) - 1):
#             # ls = 
            
#             temp_h = hFences[i] - hFences[i - 1]
#             print("temp_h, width: ", temp_h, width)

#             if temp_h == width:
#                 print("1!")
#                 mx = max(mx, temp_h * width)
#             for j in range(1, len(vFences) - 1):
#                 print("i, j, hFences[i], vFences[j]: ", i, j, hFences[i], vFences[j])
#                 temp_w = vFences[j] - vFences[j - 1]
#                 print("temp_h, temp_w: ", temp_h, temp_w)
#                 if temp_h == temp_w:
#                     print("2!")
#                     mx = max(mx, temp_h * temp_w)

                
#             print("---end of iteration---")

            
#         height = m
#         width = n
            
#         for i in range(1, len(vFences) - 1):
#             # ls = 
            
#             temp_w = vFences[i] - vFences[i - 1]
#             print("heigh, temp_w: ", height, temp_w)

#             if height == temp_w:
#                 print("1!")
#                 mx = max(mx, (height - 1) * (temp_w - 1))
#             for j in range(1, len(hFences) - 1):
#                 print("i, j, vFences[i], hFences[j]: ", i, j, vFences[i], hFences[j])
#                 temp_h = hFences[j] - hFences[j - 1]
#                 print("temp_h, temp_w: ", temp_h, temp_w)
#                 if temp_h == temp_w:
#                     print("2!")
#                     mx = max(mx, (temp_h - 1) * (temp_w - 1))
#         print("---end---")
#         return mx

        
        
        

#         hFences.sort()
#         vFences.sort()
        
#         mx = -1
#         # m -= 1
#         # n -= 1
#         height = m
#         width = n
#         print("height, width: ", height, width)
        
#         if m == n:
#             return (m - 1) * (n - 1)
        
#         hFences.insert(0, 0)
#         vFences.insert(0, 0)
#         print("hFences, vFences: ", hFences, vFences)
        
#         # temp_h = m
#         # temp_w = n
#         for i in range(len(hFences)):
#             temp_h = m - hFences[i]
#             print("temp_h, width: ", temp_h, width)

#             # if temp_h == width:
#             #     mx = max(mx, (temp_h - 1) * (width - 1))

#             for j in range(len(vFences)):

#                 print("i, j, hFences[i], vFences[j]: ", i, j, hFences[i], vFences[j])
#                 temp_w = n - vFences[j]
#                 print("temp_h, temp_w: ", temp_h, temp_w)
#                 if temp_h == temp_w:
#                     mx = max(mx, (temp_h - 1) * (width - 1))

                
#             print("---end of iteration---")
#         print("---end---")
#         return mx
    
