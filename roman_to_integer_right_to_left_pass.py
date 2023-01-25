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



Approach 3: Right-to-Left Pass
Intuition

This approach is a more elegant variant of Approach 1. Just to be clear though, Approach 1 and Approach 2 are probably sufficient for an interview. 
This approach is still well worth understanding though.

In the "subtraction" cases, such as XC, we've been updating our running sum as follows:

sum += value(C) - value(X)

However, notice that this is mathematically equivalent to the following:

sum += value(C)
sum -= value(X)
Utilizing this means that we can process one symbol each time we go around the main loop. We still need to determine whether or not our current symbol should 
be added or subtracted by looking at the neighbour though.

In Approach 1, we had to be careful when inspecting the next symbol to not go over the end of the string. This check wasn't difficult to do, but it increased the 
code complexity a bit, and it turns out we can avoid it with this approach!

Observe the following:

Without looking at the next symbol, we don't know whether or not the left-most symbol should be added or subtracted.
The right-most symbol is always added. It is either by itself, or the additive part of a pair.
So, what we can do is initialise sum to be the value of the right-most (last) symbol. Then, we work backwards through the string, starting from the second-to-last-symbol. 
We check the symbol after (i + 1) to determine whether the current symbol should be "added" or "subtracted".

Because we're starting at the second-to-last-index, we know that index i + 1 always exists. We no longer need to handle its potential non-existence as a special case, and additionally we're 
able to (cleanly) use a for loop, as we're always moving along by 1 index at at time, unlike before where it could have been 1 or 2.

Here is an animation of the above approach.




Complexity Analysis

Time complexity : O(1)O(1)O(1).
Same as Approach 1.

Space complexity : O(1)O(1)O(1).
Same as Approach 1.

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

        total = values.get(s[-1])  # total = values[s[-1]]
        for i in reversed(range(len(s) - 1)):
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total



def main():
    s = "MCMXCIV"
    result = Solution()
    print(result.romanToInt(s))


if __name__== "__main__" :
    main()