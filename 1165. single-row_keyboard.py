class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        # print("ord('a'):", ord("a"))
        # print("ord('z'):", ord("z"))

        time = 0
        cur_i = 0
        for i in range(len(word)):
            print("keyboard.find(word[i]): ", keyboard.find(word[i]))
            temp = abs(cur_i - keyboard.find(word[i]))
            time += temp
            cur_i = keyboard.find(word[i])
        return time
    
def main(keyboard, word):
    result = Solution()
    print(result.calculateTime(keyboard, word))

if __name__== "__main__" :
    keyboard = "abcdefghijklmnopqrstuvwxyz"
    word = "cba"
    main(keyboard, word)
