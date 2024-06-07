
# LeetCode 347. Top K Frequant Elements

This repository contains two solutions for the LeetCode problem 347, "Top K Frequant Elements"


## Problem Statement
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



## Solution 1 (1.py) [BruteForce_Solution]

```bash
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newarr = []  
        arr = defaultdict(int)
        
        for i in nums:
            arr[i] += 1
        
        for j in range(k):
            maxx = max(arr.values())
            for key, val in list(arr.items()):  
                if val == maxx:
                    newarr.append(key)
                    del arr[key]
                    break  
        
        return newarr



```

## Solution 2 (2.py) [Optimal_Solution]

```bash
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        count = Counter(nums)
        
        # Step 2: Use a min-heap to keep track of the top k elements
        # heapq.nlargest can directly give us the k largest elements based on their frequencies
        return [item for item, frequency in heapq.nlargest(k, count.items(), key=lambda x: x[1])]



```
  

## Time Complexity Comparison

**Solution 1:**

Counting Frequencies:

* Iterates through nums once to build the frequency dictionary.
* Time complexity: O(n) where n is the length of nums.

Finding the Top k Frequent Elements:

* For each of the k iterations, finds the maximum frequency in the dictionary.

* Time complexity for each iteration: O(m), where m is the number of unique elements.
* Total time complexity for this step: O(k⋅m).

Deleting Elements:

* Deletion from the dictionary is O(1), done k times.
* Total time complexity: O(k).

Overall Time Complexity: O(n+k⋅m).



**Solution 2:**

Counting Frequencies:

* Uses Counter to count frequencies in one pass.
* Time complexity: O(n).

Finding the Top k Frequent Elements:

* Builds a heap of the m unique elements.
* Time complexity: O(m).
* Extracting the top k elements using heapq.nlargest.
* Time complexity: O(klogm).

Overall Time Complexity: O(n+m+klogm).

## Comparison
Counting Frequencies:

* Both solutions: O(n). 

Finding the Top k Elements:

* Solution 1: O(k⋅m), linear scan for max frequency k times.
* Solution 2: O(m+klogm), using a heap for more efficient extraction..


## Acknowledgements

 - [Leetcode link](https://leetcode.com/problems/top-k-frequent-elements/)
 - [Neetcode link](https://neetcode.io/problems/top-k-elements-in-list)