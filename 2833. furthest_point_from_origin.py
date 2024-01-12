from collections import Counter

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        d = 0
        c = Counter(moves)
        dash = c["_"]
        # print("dash: ", dash)
        if c["L"] >= c["R"]:
            return c["L"] + dash - c["R"]            
        else:
            return c["R"] + dash - c["L"]

def main(moves):
    result = Solution()
    print(result.furthestDistanceFromOrigin(moves))

if __name__== "__main__" :
    moves = "L_RL__R"
    main(moves)
