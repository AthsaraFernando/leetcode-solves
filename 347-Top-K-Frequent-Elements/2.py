from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        count = Counter(nums)
        
        # Step 2: Define a helper function to extract frequency for heapq
        def get_frequency(item):
            return item[1]
        
        # Step 3: Use a min-heap to keep track of the top k elements
        top_k = heapq.nlargest(k, count.items(), key=get_frequency)
        
        # Step 4: Extract the items from the top k elements
        result = []
        for item, frequency in top_k:
            result.append(item)
        
        return result
