
# LeetCode 1. Two Sum

This repository contains two solutions for the LeetCode problem 1, "Two Sum."


## Problem Statement

Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.


## Solution 1 (1.py) [BruteForce_Solution]

```bash
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target-nums[i] == nums[j] and i!=j:
                    lis.append(i)
                    lis.append(j)
                    return lis


```

## Solution 2 (2.py) [Optimal_Solution]

```bash
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[num] = i
        return None 

```
  

## Time Complexity Comparison

**Solution 1:**

Sorting Each Word:

* Outer loop (for i in range(len(nums))): Runs n times.
* Inner loop (for j in range(len(nums))): Runs n times for each iteration of the outer loop.
* Total Time Complexity:  O(n^2) 

**Solution 2:**

Sorting Each Word:

* Single loop (for i, num in enumerate(nums)): Runs n times.
* Hash map operations:
* Checking if an item is in the hash map (complement in num_map) is O(1) on average.
* Inserting an item into the hash map (num_map[num] = i) is O(1) on average.
* Total Time Complexity: O(n) because each operation inside the loop (checking and inserting) is O(1), and the loop runs n times.


## Comparison

* Efficiency: Solution 2 is more efficient than Solution 1. Solution 1 has a time complexity of O(n^2), making it much slower for large input sizes compared to Solution 2, which has a time complexity of O(n).

* Space Usage: Solution 1 uses O(1) auxiliary space, which is more space-efficient than Solution 2's O(n) space complexity. However, this difference is generally negligible given the significant time efficiency gain with Solution 2.

* Practical Performance: In practice, Solution 2 is preferred due to its linear time complexity, which makes it scalable and performant for large datasets. The additional space requirement of Solution 2 is typically justified by its much faster execution time.

## Acknowledgements

 - [Leetcode link](https://leetcode.com/problems/two-sum/)
 - [Neetcode link](https://neetcode.io/problems/two-integer-sum)