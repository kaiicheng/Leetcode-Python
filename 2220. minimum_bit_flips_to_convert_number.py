class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        # Hamming Distance
        # Hamming Distance between two integers is the number of bits that are different at the same position in both numbers
        # print("bin(start): ", bin(start))
        # print("bin(goal): ", bin(goal))
        # print("bin(start ^ goal): ", bin(start ^ goal))
        return bin(start ^ goal).count("1")

def main(start, goal):
    result = Solution()
    print(result.minBitFlips(start, goal))

if __name__== "__main__" :
    start = 10
    goal = 7
    main(start, goal)
