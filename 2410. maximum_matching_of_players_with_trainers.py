from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        # print("players: ", players)
        trainers.sort()
        # print("trainers: ", trainers)

        ans = 0
        for i in range(len(players)):
            for j in range(len(trainers)):
                if players[i] <= trainers[j]:
                    ans += 1
                    del trainers[j]
                    break
        return ans

def main(players, trainers):
    result = Solution()
    print(result.matchPlayersAndTrainers(players, trainers))

if __name__== "__main__" :
    players = [4,7,9]
    trainers = [8,2,5,8]
    main(players, trainers)
