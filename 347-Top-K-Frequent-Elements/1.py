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

