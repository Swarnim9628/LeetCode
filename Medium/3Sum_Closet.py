class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min1=1000000
        nums.sort()
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while(j<k):
                v=(nums[i]+nums[j]+nums[k])-target
                if abs(v)<=abs(min1):
                    min1=v
                if v==0:
                    return target
                if v<0:
                    j+=1
                else:
                    k-=1
        return target+min1