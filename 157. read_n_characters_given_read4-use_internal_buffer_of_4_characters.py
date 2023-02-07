"""
Approach 1: Use Internal Buffer of 4 Characters

Algorithm

Let's use an internal buffer of 4 characters to solve this problem:
File -> Internal Buffer of 4 Characters -> Buffer of N Characters.
    - Initialize the number of copied characters copiedChars = 0, and the number of read characters: readChars = 4. It's convenient initialize readChars to 4 and then 
    use readChars != 4 as EOF marker.
    - Initialize an internal buffer of 4 characters: buf4.
    - While number of copied characters is less than N: copiedChars < n and there are still characters in the file: readChars == 4:
        - Read from file into internal buffer: readChars = read4(buf4).
        - Copy the characters from internal buffer buf4 into main buffer buf one by one. Increase copiedChars after each character. In the number of copied characters 
        is equal to N: copiedChars == n, interrupt the copy process and return copiedChars.



Complexity Analysis

Time complexity: O(N) to copy N characters.

Space complexity: O(1) to keep buf4 of 4 elements.
"""

from typing import List

"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        copied_chars = 0
        read_chars = 4
        buf4 = [''] * 4
        
        while copied_chars < n and read_chars == 4:
            read_chars = read4(buf4)
            
            for i in range(read_chars):
                if copied_chars == n:
                    return copied_chars
                buf[copied_chars] = buf4[i]
                copied_chars += 1
        
        return copied_chars

def main():
    file = "abcdABCD1234"
    n = 12
    result = Solution()
    print(result.read(file, n))


if __name__== "__main__" :
    main()