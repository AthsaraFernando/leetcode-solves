from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        count = Counter(nums)
        
        # Step 2: Use a min-heap to keep track of the top k elements
        # heapq.nlargest can directly give us the k largest elements based on their frequencies
        return [item for item, frequency in heapq.nlargest(k, count.items(), key=lambda x: x[1])]

