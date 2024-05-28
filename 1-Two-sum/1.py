class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target-nums[i] == nums[j] and i!=j:
                    lis.append(i)
                    lis.append(j)
                    return lis
                
