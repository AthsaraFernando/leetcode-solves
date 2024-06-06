
# LeetCode 217. Contain Duplicate

This repository contains solution for the LeetCode problem 217, "Contains Dupcliate."


## Problem Statement

Given an array of integers, determine if the array contains any duplicates. Return True if any value appears at least twice in the array, and False if every element is distinct.


## Solution 1 (1.py) [Optimal_Solution]

```bash
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


```
  

## Time Complexity Comparison

**Solution 1:**

* Iteration over the list:
Time Complexity: O(n)
* Checking and adding elements to the set:
Time Complexity: O(1) on average per operation

* Overall Time Complexity: O(n)


## Acknowledgements

 - [Leetcode link](https://leetcode.com/problems/contains-duplicate/description/)
 - [Neetcode link](https://neetcode.io/problems/duplicate-integer)