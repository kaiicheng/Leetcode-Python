from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0:
            return True

        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n <= 1:
                return True
            else:
                return False
            
        if len(flowerbed) == 2:
            if n > 1:
                return False
            else:
                if flowerbed[0] == 0 and flowerbed[1] == 0:
                    return True
                else:
                    return False
            

        for i in range(len(flowerbed)):
            # print("i: ", i)
            # print("flowerbed[i]: ", flowerbed[i])
            # print("n: ", n)

            if n <= 0:
                return True
            else:
                if i == 0:
                    if flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                        # print("1!")
                        # print("flowerbed[i]: ", flowerbed[i])
                        flowerbed[i] = 1
                        n -= 1
                        # print("flowerbed: ", flowerbed)

                elif i == len(flowerbed) - 1:
                    if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                        # print("in!")
                        flowerbed[i] = 1
                        n -= 1
                else: 
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] != 1:
                        flowerbed[i] = 1
                        n -= 1
            # print("flowerbed: ", flowerbed)
        if n <= 0:
            return True
        else:
            return False

def main(flowerbed, n):
    result = Solution()
    print(result.canPlaceFlowers(flowerbed, n))

if __name__== "__main__" :
    # flowerbed = [1,0,0,0,0,1]
    # n = 2
    # flowerbed = [1,0,1,0,1,0,1]
    # n = 1
    # flowerbed = [0,0,1,0,1]
    # n = 1
    # flowerbed = [1,0,0,0,1]
    # n = 2
    # flowerbed = [1,0,0,0,1,0,0]
    # n = 2
    # flowerbed = [0,0]
    # n = 2
    flowerbed = [0,0,0,0]
    n = 3
    main(flowerbed, n)
