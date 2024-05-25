
# LeetCode 242. Valid Anagram

This repository contains two solutions for the LeetCode problem 242, "Valid Anagram."


## Problem Statement

Given two strings s and t, write a function to determine if t is an anagram of s.



## Solution 1 (1.py)

```bash
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist=[]
        tlist=[]
        if len(s)==len(t):
            for i in s:
                slist.append(i)
            
            for i in t:
                tlist.append(i)

            for j in slist:
                for k in range(len(tlist)):
                    if j==tlist[k]:
                        tlist.remove(tlist[k])
                        break

            if len(tlist)!=0:
                return False
            else:
                return True


```

## Solution 1 (2.py)

```bash
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        return count_s == count_t

```
  

## Time Complexity Comparison

Solution 1:

This solution manually compares characters of the two strings by building two lists and then removing matching characters from one list based on the other.

  Time Complexity: O(n2)O(n2)
        The outer loops that build slist and tlist are O(n)O(n).

        The nested loops where each character in slist is compared with each character in tlist result in O(n2)O(n2) operations in the worst case (where nn is the length of the strings).

Solution 2:

This solution counts the frequency of each character in both strings and then compares these frequency counts.

  Time Complexity: O(n)O(n)
  
        The loops that count the characters in s and t are both O(n)O(n).
        Comparing the two dictionaries is O(n)O(n) in the average case.

## Comparison

  Solution 1 is simpler but less efficient with a time complexity of O(n2)O(n2). It manually handles character matching and removal.


  Solution 2 is more efficient with a time complexity of O(n)O(n). It uses dictionaries to count character frequencies and then compares these counts.

## Acknowledgements

 - [Leetcode link](https://leetcode.com/problems/valid-anagram/)
 - [Neetcode link](https://neetcode.io/problems/is-anagram)