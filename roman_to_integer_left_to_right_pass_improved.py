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



Approach 2: Left-to-Right Pass Improved
Intuition

Instead of viewing a Roman Numeral as having 7 unique symbols, we could instead view it as having 13 unique symbols—some of length-1 and some of length-2.

For example, here is the Roman Numeral MMCMLXXXIX broken into its symbols using this definition:

We can then look up the value of each symbol and add them together.

After making a Map of String -> Integer with the 13 "symbols", we need to work our way down the string in the same way as before (we'll do left-to-right, however right-to-left will work okay too), 
firstly checking if we're at a length-2 symbol, and if not, then treating it as a length-1 symbol.



# Complexity Analysis

# Time complexity : O(1)O(1)O(1).
# Same as Approach 1.

# Space complexity : O(1)O(1)O(1).
# Same as Approach 1.

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
    "IV": 4,
    "IX": 9,
    "XL": 40, 
    "XC": 90,
    "CD": 400,
    "CM": 900
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
            # This is the subtractive case.
            if i < len(s) - 1 and s[i:i+2] in values:
                total += values[s[i:i+2]] 
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total


def main():
    s = "MCMXCIV"
    result = Solution()
    print(result.romanToInt(s))


if __name__== "__main__" :
    main()