class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            r=target-nums[i]
            
            if r in nums and nums.index(r)!=i:
                return [i,nums.index(r)]