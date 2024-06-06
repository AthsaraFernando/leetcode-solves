
# LeetCode 242. Valid Anagram

This repository contains two solutions for the LeetCode problem 49, "Group Anagram."


## Problem Statement

Given an array of strings, you need to group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



## Solution 1 (1.py)

```bash
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        out2 = []
        flag = []

        for k in strs:
            sorted_strs.append(''.join(sorted(k)))  # Sorting each word

        for i in range(len(sorted_strs)):
            if sorted_strs[i] not in flag:
                out1 = [strs[i]]  # Initialize with the original word
                for j in range(len(sorted_strs)):
                    if i != j and sorted_strs[i] == sorted_strs[j]:
                        flag.append(sorted_strs[j])
                        out1.append(strs[j])
                out2.append(out1)
                flag.append(sorted_strs[i])  # Add the current word's sorted version to the flag

        return out2
'''
# Example usage
solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(strs))
'''


```

## Solution 2 (2.py)

```bash
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # Dictionary to hold lists of anagrams
        
        for word in strs:
            sorted_word = ''.join(sorted(word))  # Sort the word to use as a key
            anagrams[sorted_word].append(word)  # Append the original word to the correct list
        
        return list(anagrams.values())  # Return the grouped anagrams as a list of lists

'''
# Example usage
solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(strs))
'''

```
  

## Time Complexity Comparison

**Solution 1:**

Sorting Each Word:

* This operation is O(K log K), where K is the length of the word.
* This is done for each of the N words.
* Total time for sorting: O(N * K log K).

Nested Loop for Comparison:

* The outer loop runs N times.
* The inner loop also runs N times.
* Comparison of sorted strings takes O(K) time in the worst case.
* Total time for comparison: O(N^2 ** K).

Overall Time Complexity:

* Combining both parts: O(N * K log K) + O(N^2 * K).
* Dominated by the quadratic term: O(N^2 * K).

**Solution 2:**

Sorting Each Word:

* This operation is O(K log K), where K is the length of the word.
* This is done for each of the N words.
* Total time for sorting: O(N * K log K).

Inserting into Dictionary:

* Dictionary insertion is O(1) on average.
* This is done for each of the N words.
* Total time for insertion: O(N).

Overall Time Complexity:

* Total: O(N * K log K) for sorting each word and O(N) for inserting into the dictionary.
* Dominated by the sorting: O(N * K log K).

## Comparison

* Original Solution: O(N * K log K) + O(N^2 * K) → Dominated by O(N^2 * K).
* Optimized Solution: O(N * K log K).

The optimized solution is significantly more efficient, particularly for large values of N. The original solution has a quadratic complexity with respect to N, which can become infeasible for large datasets, while the optimized solution has a linearithmic complexity, making it much more scalable.

## Acknowledgements

 - [Leetcode link](https://leetcode.com/problems/group-anagrams/)
 - [Neetcode link](https://neetcode.io/problems/anagram-groups)