"""

Can we assume the input is valid?

Yes. Here on Leetcode, you can make that assumption because you haven't been told what to do if it isn't.
In a real interview, this is a question you should ask the interviewer. Don't ever assume without asking in a real interview that the input has to be valid.



Is there only one valid representation for each number?

This is more relevant to the other question, Integer to Roman, however we'll still briefly look at it now.

Given that the representation for 3 is III, it could seem natural that the representation for 15 is VVV, because that would be 5 + 5 + 5. However, it's actually 
XV, which is 10 + 5. How are you even supposed to know which is correct?

The trick is to use the "biggest" symbols you can. Because X is bigger than V, we should use an X first and then make up the remainder with a single V, giving XV.

We'll talk more about this in the Integer to Roman article. This question is a lot simpler because there's only one logical way of converting from a Roman Numeral 
to an Integer. This is also why this question is labelled as "easy", whereas the other is



A few more examples

If you're not very familiar with Roman Numerals, work through these examples and then have another go at writing your own algorithm before reading 
the rest of this solution article.

What is CXVII as an integer?

Recall that C = 100, X = 10, V = 5, and I = 1. Because the symbols are ordered from most significant to least, we can simply add the symbols, 
i.e. C + X + V + I + I = 100 + 10 + 5 + 1 + 1 = 117.

What is DXCI as an integer?

Recall that D = 500.

Now, notice that this time the symbols are not ordered from most significant to least—the X and C are out of numeric order. Because of this, we subtract 
the value of X (10) from the value of C (100) to get 90.

So, going from left to right, we have D + (C - X) + I = 500 + 90 + 1 = 591.

What is CMXCIV as an integer?

Recall that M = 1000.

The symbols barely look sorted at all here—from left-to-right we have 100, 1000, 10, 100, 1, 5. Do not panic though, we just need to look for each occurrence 
of a smaller symbols preceding a bigger symbol. The first, third, and fifth symbols are all smaller than their next symbol. Therefore they are all going to be 
subtracted from their next.

The first two symbols are CM. This is M - C = 1000 - 100 = 900
The second two symbols are XC. This is C - X = 100 - 10 = 90.
The final two symbols are IV. This is V - I = 5 - 1 = 4.
Like we did above, we add these together. (M - C) + (C - X) + (V - I) = 900 + 90 + 4 = 994.



Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.



Approach 1: Left-to-Right Pass
Intuition

Let's hard-code a mapping with the value of each symbol so that we can easily look them up.

Now, recall that each symbol adds its own value, except for when a smaller valued symbol is before a larger valued symbol. In those cases, instead of adding both 
symbols to the total, we need to subtract the large from the small, adding that instead.

Therefore, the simplest algorithm is to use a pointer to scan through the string, at each step deciding whether to add the current symbol and go forward 1 place, or 
add the difference of the next 2 symbols and go forward 2 places. Here is this algorithm in pseudocode.

Here is an animation of the above algorithm.

Recall that the input is always valid. This means that we don't need to worry about being given inputs such as ICD.



Complexity Analysis

Let n be the length of the input string (the total number of symbols in it).

Time complexity : O(1)z.
As there is a finite set of roman numerals, the maximum number possible number can be 3999, which in roman numerals is MMMCMXCIX. As such the time complexity is O(1).

If roman numerals had an arbitrary number of symbols, then the time complexity would be proportional to the length of the input, i.e. O(n). This is assuming that 
looking up the value of each symbol is O(1).

Space complexity : O(1).
Because only a constant number of single-value variables are used, the space complexity is O(1).

"""


from typing import List

values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        total = 0
        i = 0
        while i < len(s):
            # if this is the subtractive case.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # else this is NOT the subtractive case.
            else:
                total += values[s[i]]
                i += 1
            # print("total:", total)
            # print("i:", i)
        return total



def main():
    s = "MCMXCIV"
    result = Solution()
    print(result.romanToInt(s))


if __name__== "__main__" :
    main()