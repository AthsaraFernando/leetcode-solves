from typing import List

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