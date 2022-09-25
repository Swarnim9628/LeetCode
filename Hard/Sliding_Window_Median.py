class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        st=0
        sum1=0
        i=0
        temp=[]
        ans=[]
        while i<len(nums):
            temp.append(nums[i])
            if len(temp)>=k:
                if k%2!=0:
                    a=k//2
                    temp.sort()
                    ans.append(temp[a])
                    temp.remove(nums[st])
                    st+=1
                else:
                    temp.sort()
                    a=k//2
                    b=a-1
                    print((temp[a]+temp[b])/2)
                    ans.append((temp[a]+temp[b])/2)
                    temp.remove(nums[st])
                    st+=1
            i+=1