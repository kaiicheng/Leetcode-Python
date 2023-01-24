# Algorithm

# It turns out we can do it in one-pass. While we are iterating and inserting elements into the 
# hash table, we also look back to check if current element's complement already exists in the 
# hash table. If it exists, we have found a solution and return the indices immediately.

# Complexity Analysis

# Time complexity: O(n). We traverse the list containing nn elements only once. 
# Each lookup in the table costs only O(1) time.

# Space complexity: O(n). The extra space required depends on the number of items 
# stored in the hash table, which stores at most n elements.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]  # hashmap[2] = 0
            hashmap[nums[i]] = i  # hashmap = {2: 0, 7: 1, 11: 2, 15: 3}

def main():
    nums = [2, 0, 50, 12, 11, 15, 7]
    target = 9
    result = Solution()
    print(result.twoSum(nums, target))


if __name__== "__main__" :
    main()