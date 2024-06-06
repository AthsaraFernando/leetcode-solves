from typing import List
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