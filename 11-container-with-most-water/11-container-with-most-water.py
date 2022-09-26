class Solution:
    def maxArea(self, h: List[int]) -> int:
        m=-math.inf
        i=0
        j=len(h)-1
        while i!=j:
            
            a=min(h[i],h[j])
            b=abs(i-j)
            m=max(m,a*b)
            if h[i]>=h[j]:
                j-=1
            else:
                i+=1
        return m
            
            
        