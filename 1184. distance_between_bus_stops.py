from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        if start < destination:
            a = sum(distance[start:destination])
            b = sum(distance[destination:]) +  sum(distance[:start])
        elif start > destination:
            a = sum(distance[destination:start])
            b = sum(distance[start:]) +  sum(distance[:destination])
        print("a, b: ", a, b)
        return min(a, b)

def main(distance, start, destination):
    result = Solution()
    print(result.distanceBetweenBusStops(distance, start, destination))

if __name__== "__main__" :
    distance = [1,2,3,4]
    start = 0
    destination = 1
    main(distance, start, destination)