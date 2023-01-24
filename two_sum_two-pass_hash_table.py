# Intuition

# To improve our runtime complexity, we need a more efficient way to check if the complement exists 
# in the array. If the complement exists, we need to get its index. What is the best way to maintain 
# a mapping of each element in the array to its index? A hash table.

# We can reduce the lookup time from O(n)O(n) to O(1)O(1) by trading space for speed. A hash table 
# is well suited for this purpose because it supports fast lookup in near constant time. I say "near" 
# because if a collision occurred, a lookup could degenerate to O(n)O(n) time. However, lookup in a 
# hash table should be amortized O(1)O(1) time as long as the hash function was chosen carefully.

# Algorithm

# A simple implementation uses two iterations. In the first iteration, we add each element's value 
# as a key and its index as a value to the hash table. Then, in the second iteration, we check if 
# each element's complement (target - nums[i]target−nums[i]) exists in the hash table. If it does 
# exist, we return current element's index and its complement's index. Beware that the complement 
# must not be nums[i]nums[i] itself!

# Complexity Analysis

# Time complexity: O(n)O(n). We traverse the list containing nn elements exactly twice. Since the 
# hash table reduces the lookup time to O(1)O(1), the overall time complexity is O(n)O(n).

# Space complexity: O(n)O(n). The extra space required depends on the number of items stored in 
# the hash table, which stores exactly nn elements.

# nums = [2, 7, 11, 15]
# target = 9

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i  # hashmap = {2: 0, 7: 1, 11: 2, 15: 3}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:  # Beware that the complement must not be nums[i]nums[i]nums[i] itself!
                return [i, hashmap[complement]]    # hashmap[2] = 0

def main():
    nums = [2, 0, 50, 12, 11, 15, 7]
    target = 9
    result = Solution()
    print(result.twoSum(nums, target))


if __name__== "__main__" :
    main()