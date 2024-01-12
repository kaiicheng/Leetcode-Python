class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        cat = None

        bulky = False
        if length >= 10000 or width >= 10000 or height >= 10000 or length * width * height >= 10 ** 9:
            bulky = True

        heavy = False
        if mass >= 100:
            heavy = True
        
        if bulky and heavy:
            cat = "Both"
        elif not bulky and not heavy:
            cat = "Neither"
        elif bulky and not heavy:
            cat = "Bulky"
        elif not bulky and heavy:
            cat = "Heavy"

        return cat

def main(length, width, height, mass):
    result = Solution()
    print(result.categorizeBox(length, width, height, mass))

if __name__== "__main__" :
    length = 1000
    width = 35
    height = 700
    mass = 300
    main(length, width, height, mass)